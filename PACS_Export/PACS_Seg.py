import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
# reading in dicom files
import pydicom  # DICOM Images (.dicom)
import torch

##########################################################
# Bilderserien
##########################################################

# -------------------Load------------------------------
def load_scan(path):  # DICOM Bild einlesen
    slices = [pydicom.dcmread(path + '/' + s) for s in
              os.listdir(path)]
    # print(slices)
    slices = [s for s in slices if 'SliceLocation' in s]
    slices.sort(key=lambda x: int(x.InstanceNumber), reverse=True)
    try:
        slice_thickness = np.abs(slices[0].ImagePositionPatient[2] -
                                 slices[1].ImagePositionPatient[2])
    except:

        slice_thickness = np.abs(slices[0].SliceLocation - slices[1].SliceLocation)

    for s in slices:
        s.SliceThickness = slice_thickness
    return slices

# use this if you want to normalize or denormalize the images.
def interval_mapping(image, from_min, from_max, to_min, to_max):
    # map values from [from_min, from_max] to [to_min, to_max]
    # image: input array
    from_range = from_max - from_min
    to_range = to_max - to_min
    scaled = np.array((image - from_min) / float(from_range), dtype=float)
    return to_min + (scaled * to_range)

 #-----------DICOM to Pixel------------------------------------------------
def get_pixels_hu(scans):

    image = np.stack([s.pixel_array for s in scans])
    image = image.astype(np.int16)
    # Set outside-of-scan pixels to 0
    # The intercept is usually -1024, so air is approximately 0
    image[image == -2000] = 0

    # Convert to Hounsfield units (HU)
    intercept = scans[0].RescaleIntercept if 'RescaleIntercept' in scans[0] else -1024
    slope = scans[0].RescaleSlope if 'RescaleSlope' in scans[0] else 1

    if slope != 1:
        image = slope * image.astype(np.float64)
        image = image.astype(np.int16)

    image += np.int16(intercept)
    return np.array(image, dtype=np.int16)


    # ----save---------------------------------------------------------
def save(path, name, image):
    image = torch.from_numpy(image)

    image = image.to(torch.float16)
    image = image.unsqueeze(0)

    path = path + "/" + "serie.pt"  # Mit patienten ID speicher:  path = path + "/" + "serie_" + str(i) + ".pt"
    torch.save({"vol": image, "id": name}, path)


##########################################################
# Segmentieung
##########################################################


def dicom_ROI_extract(path):
    # ---------------- Dicom File Laden ----------------------------------------------------------------
    ds = pydicom.read_file(path)  # Einlesen des DICOM Files zur Segmentierung
    # print(ds)
    # --------------- ROIs ------------------------------------------------------------------------------
    coords = []
    uids_ROI = []
    name_ROI = []
    flag = 0
    for i in range(100):  # Durchläuft die ROIs

        try:
            ds['0070', '0001'][i]  # schaut ob es das Element ite gibt (also ob es noch eine weitere ROI gibt)
        except IndexError:  # wenn nicht stoppt die Schleife
            break
        else:

            # this is necessary because recist measurements and texts are also saved as a roi.
            first_list_item = ds['0070', '0001'][i]
            try:
                first_list_item['0070', '0009'] # Wenn es das nicht gibt dann ist es keine ROI
                # for item in first_list_item['0070', '0008']:
                #     hold = (item['0070', '0006'].value)  # ROI Name und Infos
                # if "mm2" not in hold:
                #     raise Exception()
            except:
                print("no ROI")
            else:

                for item in first_list_item['0070', '0009']: # durchläuft Graphic Object Sequence (Eventuell gibt es da mehrere ROIs)
                    test = item['0070', '0023'].value
                    if item['0070', '0023'].value == 'INTERPOLATED': # Wenn (0070, 0023) Graphic Type nicht 'INTERPOLATED' ist es keine ROI
                        flag = 1
                        coords.append(item['0070', '0022'].value)  # Koordinaten der ROI
                if flag == 1:
                    for item in first_list_item['0008', '1140']:
                            uids_ROI.append(item['0008', '1155'].value)  # SOP Instance UID für Schichtnummer der ROI
                    # for item in first_list_item['0070', '0008']:
                    #         name_ROI.append(item['0070', '0006'].value)  # ROI Name und Infos
                flag = 0

    coords = np.array(coords)  # numpy array mit Koordinaten jeder ROI
    uids_ROI = np.array(uids_ROI)  # numpy array mit UID jeder ROI
    #name_ROI = np.array(name_ROI)  # numpy array mit name und Infos jeder ROI

    return coords, uids_ROI, name_ROI, ds
#1.3.12.2.1107.5.2.19.45218.2020092410100072918827383

# ---------------Koordinaten als Tupel-------------------------------------------------------
def get_tuple(coords):
    coords_tuple = ()
    for i in range(0, len(coords) - 1, 2):
        coords_tuple = coords_tuple + ((coords[i], coords[i + 1]),)
    return (coords_tuple)


    # ---------------Centroid (wird aktuell nicht verwendet)--------------------------------------
def get_centroid(polygon):
    A = 0
    x_s = 0
    y_s = 0
    for i in range(len(polygon) - 1):
        A += 0.5 * (polygon[i][0] * polygon[i + 1][1] - polygon[i + 1][0] * polygon[i][1])
    for i in range(len(polygon) - 1):
        x_s += 1 / (6 * A) * (polygon[i][0] + polygon[i + 1][0]) * (
                polygon[i][0] * polygon[i + 1][1] - polygon[i + 1][0] * polygon[i][1])

    for i in range(len(polygon) - 1):
        y_s += 1 / (6 * A) * (polygon[i][1] + polygon[i + 1][1]) * (polygon[i][0] * polygon[i + 1][1] - polygon[i + 1][0] * polygon[i][1])
    return (x_s, y_s)

 # ---------ROIs zu Maske -----------------------------------------------------------------------------
def save_rois(ds, centroid, uids_ROI, name_ROI, coords, path, patient_pixels):

    uids = []
    for i in range(100):  # Durchläuft die Schichten

        try:
            ds['0008', '1115'][i]  # schaut ob es das Element ite gibt (also ob es noch eine weitere Schicht gibt gibt)
        except IndexError:  # wenn nicht stoppt die Schleife
            break
        else:
            first_list_item = ds['0008', '1115'][i]
            for item in first_list_item['0008', '1140']:
                uids.append(item['0008', '1155'].value)  # UID der Schicht
    uids = np.array(uids)

    coords_tuple = []

    # create zero numpy array.
    array = np.zeros(patient_pixels.shape)

    # find the slice location of the specific rois.
    positions = []

    for a in uids_ROI:
        positions.append(uids.tolist().index(a))

    for b in range(uids_ROI.size):

        coords_tuple.append(get_tuple(coords[b]))
        x, y = zip(*coords_tuple[b])
        fig = plt.figure(figsize=(array[1].shape), dpi=1)
        plt.xlim((0, len(array[1])))
        plt.ylim((0, len(array[1])))
        plt.plot(x, y, 'w')

        # plt.plot([0,383], [0,383], b)
        plt.fill(x, y, 'w')
        plt.axis('off')
        fig.patch.set_facecolor('xkcd:black')
        fig.tight_layout()
        #plt.savefig(path.split(".")[0] + "/" + "Maske_ROI_" + str(b) + "_matplot", facecolor='black')
        fig.canvas.draw()
        mask_data = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        tmp_array = mask_data.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        tmp_array = tmp_array[:, :, 0]
        pos = positions[b]
        tmp_array = np.array(tmp_array)
        tmp_array[tmp_array > 0] = 1
        array[pos] = tmp_array

    return array

##########################################################
# Main
##########################################################

def main():
    #--------------Vorarbeit-------------------------------------------------------

    # TODO pfade.
    path_roi = "/media/wolfda/Ashur Pro2/Postata/3559196/116/000001_1.2.40.0.13.1.239536966067868511980743902465812467956.dcm"
    path_images = "/media/wolfda/Ashur Pro2/Postata/3559196/6"

    # Create saving folder
    #Path(path_roi.split(".")[0]).mkdir(parents=False, exist_ok=True)


    #--------------Loading Images and Conversion to Torch File-----------------------

    # extract DICOM image.
    patient_dicom = load_scan(path_images)

    # Houndsfield correction to np int16.
    patient_pixels = get_pixels_hu(patient_dicom)

    # Bilderserie ist falschrum (also Bild 1 ist ganz hinten,...) deshalb flip
    patient_pixels = np.flip(patient_pixels, [0])

    patient_pixels = interval_mapping(patient_pixels, patient_pixels.min(), patient_pixels.max(), 0, 255)

    # save image.
    #save(path_roi.split(".")[0], patient_dicom[0]['0010', '0020'].value, patient_pixels)
    torch.save(patient_pixels, "serie.pt")


    #----------------Segementierung -------------------------------------------------------

    # extract roi coordinates, names and ids.
    coords, uids_ROI, name_ROI, ds = dicom_ROI_extract(path_roi)

    # calculate centroids (wird aktuell nicht verwendet)
    centroid = []
    for i in range(coords.shape[0]):
        centroid.append(get_centroid(get_tuple(coords[i])))

    # Aus rois die Maske erstellen
    mask = save_rois(ds=ds, centroid=centroid, uids_ROI=uids_ROI, name_ROI=name_ROI, coords=coords, path=path_roi, patient_pixels = patient_pixels)

    #Flips array in the left/right direction (WARUM IST DAS NÖTIG?)
    mask = np.fliplr(mask)

    # Speichern
    torch.save(mask, "mask.pt")



if __name__ == '__main__':
    main()


# Allgemeine Info:

# ROI wenn:
# ['0070', '0001'] -> ['0070', '0009'] exsitiert
# ['0070', '0001'] -> ['0070', '0009'] -> (0070, 0023) ist 'INTERPOLATED'

# Dann ROI Koordinaten: ['0070', '0001'] -> ['0070', '0009'] ->(0070, 0022)
# Und SOP Instance UID der ROI: (0008, 1140) -> (0008, 1155)
