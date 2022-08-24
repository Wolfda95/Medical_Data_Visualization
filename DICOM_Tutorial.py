# ----------packages------------------------------
import os
import numpy as np

from batchviewer import view_batch  # 3D Visualisierung (aus Git runtergeladen)

import pydicom  # DICOM Images (.dicom)



# -------------------Load DICOM Image------------------------------
def load_scan(path):

    slices = [pydicom.dcmread(path + '/' + s) for s in os.listdir(path)] #holt alle DICOM Dateien aus dem Ordner
    #slices = [s for s in slices if 'SliceLocation' in s]
    slices.sort(key=lambda x: int(x.InstanceNumber)) #InstanceNumber sagt an welcher Stelle die DICOM Datei kommen muss
    try:
        slice_thickness = np.abs(slices[0].ImagePositionPatient[2] -
                                 slices[1].ImagePositionPatient[2])
    except:

        slice_thickness = np.abs(slices[0].SliceLocation - slices[1].SliceLocation)

    for s in slices:
        s.SliceThickness = slice_thickness
    return slices


# ------------------- DICOM Image to Numpy Array (+Houndfield) ------------------------------
def get_pixels_hu(scans):  # DICOM to Pixel

    image = np.stack([s.pixel_array for s in scans])
    image = image.astype(np.int16)
    # Set outside-of-scan pixels to 0
    # The intercept is usually -1024, so air is approximately 0
    image[image == -2000] = 0

    # # Convert to Hounsfield units (HU)
    intercept = scans[0].RescaleIntercept if 'RescaleIntercept' in scans[0] else -1024
    slope = scans[0].RescaleSlope if 'RescaleSlope' in scans[0] else 1

    if slope != 1:
        image = slope * image.astype(np.float64)
        image = image.astype(np.int16)

    image += np.int16(intercept)
    return np.array(image, dtype=np.int16)


# ------------------- CT: Scale pixel intensity --------------------------------------------
# https://gist.github.com/lebedov/e81bd36f66ea1ab60a1ce890b07a6229
# abdomen: {'wl': 60, 'ww': 400} || angio: {'wl': 300, 'ww': 600} || bone: {'wl': 300, 'ww': 1500} || brain: {'wl': 40, 'ww': 80} || chest: {'wl': 40, 'ww': 400} || lungs: {'wl': -400, 'ww': 1500}
def win_scale(data, wl, ww, dtype, out_range):
    data_new = np.empty(data.shape, dtype=np.double)
    data_new.fill(out_range[1] - 1)

    data_new[data <= (wl - ww / 2.0)] = out_range[0]
    data_new[(data > (wl - ww / 2.0)) & (data <= (wl + ww / 2.0))] = \
        ((data[(data > (wl - ww / 2.0)) & (data <= (wl + ww / 2.0))] - (wl - 0.5)) / (ww - 1.0) + 0.5) * (
                out_range[1] - out_range[0]) + out_range[0]
    data_new[data > (wl + ww / 2.0)] = out_range[1] - 1

    return data_new.astype(dtype)


# ------------------- Scalierung --------------------------------------------
def min_max_normalization(data, eps):
    mn = data.min()
    mx = data.max()
    data_normalized = data - mn
    old_range = mx - mn + eps
    data_normalized /= old_range

    return data_normalized



# ------------------- DICOM Header der ersten Schicht + Visualisierung (ohne Maske)--------------------------------------------
def visualisierung(patient_dicom, patient_pixels):
    print(patient_dicom[1]) # DICOM Header der ersten Schicht
    print(patient_dicom[2])
    print(patient_dicom[3])

    patient_pixels = np.transpose(patient_pixels, (0, 2, 1))
    width = patient_pixels.shape[1]
    hight = patient_pixels.shape[2]
    view_batch(patient_pixels, width=width, height=hight)



#############################################################################################################

# ------------------- DICOM CT BatchViwer --------------------------------------------
def main():

    # Path to Folder with DICOM Images
    path = "/home/wolfda/Clinic_Data/Challenge/CT_PreTrain/LIDC/manifest-1600709154662/LIDC-IDRI/LIDC-IDRI-0001/01-01-2000-NA-NA-30178/3000566.000000-NA-03192"
    # Body: abdomen, angio, bon, brain, chest, lungs
    body_part = "lungs"

    if body_part == "abdomen":
        wl = 60
        ww = 400
        print("abdomen")
    if body_part == "angio":
        wl = 300
        ww = 600
        print("angio")
    if body_part == "bone":
        wl = 300
        ww = 150
        print("bone")
    if body_part == "brain":
        wl = 40
        ww = 80
        print("brain")
    if body_part == "chest":
        wl = 40
        ww = 400
        print("chest")
    if body_part == "lungs":
        wl = -400
        ww = 1500
        print("lungs")



    patient_dicom = load_scan(path)
    patient_pixels = get_pixels_hu(patient_dicom)  # Numpy Array (Anzahl Schichten, x,y)
    patient_pixels = win_scale(patient_pixels, wl, ww, type(patient_pixels), [patient_pixels.min(), patient_pixels.max()])  # Numpy Array Korrigiert
    patient_pixels = patient_pixels[::-1,...]  # läuft die Schichten von hinten durch, da irgendwie die Schichten umgedreht wurden

    print(patient_pixels.shape)

    visualisierung(patient_dicom, patient_pixels)

if __name__ == '__main__':
    main()