import os
import numpy as np
import matplotlib.pyplot as plt
from batchviewer import view_batch  # 3D visualization (needs to be downloaded from Git)
import pydicom  # DICOM Images (.dicom)
import nrrd # Nrrd files
import torch


# -------------------Load DICOM Image------------------------------
def load_scan(path):

    slices = [pydicom.dcmread(path + '/' + s) for s in os.listdir(path)] # Fetches all DICOM files from the folder
    slices = [s for s in slices if 'SliceLocation' in s]
    slices.sort(key=lambda x: int(x.InstanceNumber)) # InstanceNumber tells where the DICOM file must come from
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

# ------------------- Get Slice Number were the Segmentation starts from the NRRD file  ------------------------------
def load_positions(path):
    scan_high_dose = load_scan(path)
    high_dose_positions = []
    for i in range(len(scan_high_dose)):
        high_dose_positions.append(scan_high_dose[i]["ImagePositionPatient"].value[2])

    return high_dose_positions


# ------------------- 2D visualization (overlay slice + segmentation) ------------------------------
def images(img, mask):
    plt.figure(1)
    plt.imshow(img, cmap="gray")
    plt.imshow(mask, alpha=0.5, cmap="cubehelix")
    # plt.savefig("/home/wolfda/Clinic_Data/Data/Sarkome_Catharina/Data/Segmentierung/Test" + "seg" + "/" + "_" + str(x) + "_" + str(i) +".png")
    plt.show()
    plt.close()

    plt.figure(2)
    plt.imshow(img, cmap="gray")
    # plt.savefig("/home/wolfda/Clinic_Data/Data/Sarkome_Catharina/Data/Segmentierung/Text" + "img" + "/" + "_" + str(x) + "_" + str(i) +".png")
    plt.show()
    plt.close()


# ------------------- 3D visualization --------------------------------------------
def visualisierung_mask(patient_pixels, img_mask):
    # print(patient_dicom[1]) # DICOM Header of the first slice

    patient_pixels = np.transpose(patient_pixels, (0, 2, 1))
    img_mask = np.transpose(img_mask, (0, 2, 1))
    width = patient_pixels.shape[1]
    hight = patient_pixels.shape[2]
    view_batch(patient_pixels, img_mask, width=width, height=hight)




def main():

    dicom = "/media/wolfda/Ashur Pro2/VC_Hoden_multi/0003027408/Befundverlauf 1/0/Baseline/1.2.840.113704.1.111.9840.1448875333.6"
    nrrdx = "/media/wolfda/Ashur Pro2/VC_Hoden_multi/0003027408/Befundverlauf 1/0/Baseline/1.2.840.113704.1.111.9840.1448875333.6_F01 lis_generic_primary_primary_3026345.nrrd"


    # Load DICOM
    patient_dicom = load_scan(dicom)
    patient_pixels = get_pixels_hu(patient_dicom)  # Numpy Array (Slices, x,y)
    #patient_pixels = win_scale(patient_pixels, wl, ww, type(patient_pixels), [patient_pixels.min(), patient_pixels.max()])  # Numpy Array Korrigiert
    patient_pixels = patient_pixels.astype(np.float32)
    # print(patient_pixels.shape)

    # Load Nrrd
    readdata, header = nrrd.read(nrrdx)
    readdata = np.transpose(readdata, (2, 0, 1))
    # print(readdata.shape)
    # print(header)

    # Extract DICOM Tag "ImagePositionPatient" for all slices
    dicom = load_positions(dicom)

    # Extract Nrrd Tag 'space origin' (the volume of the Nrrd file starts here)
    position_nrrd = header["space origin"][2]
    # round the number.
    position_nrrd = float(position_nrrd)
    position_nrrd = round(position_nrrd, 3)

    # Find the slice where the Nrrd space starts
    for i in range(len(dicom)):
        if position_nrrd == round(dicom[i], 3):
            slice_number = i

    # create an empty cube with the image dimensions.
    size = patient_pixels.shape  # (233, 512, 512)
    cube = np.zeros(size)
    cube = np.flip(cube, 0)

    # Number of layers Nrrd File
    z = readdata.shape[0] - 1  # -1 since it starts with zero
    # print("slice Number", slice_number)
    # print("slice Number - z", slice_number-z)

    # insert the nrrd array in the right place.
    for i in range(slice_number - z, slice_number + 1):
        cube[i] = np.rot90(np.flipud(readdata[z]), 3)  # Schicht 8,7,6... [90 degree rotation]
        images(patient_pixels[i], cube[i]) # 2D Visualization
        # print(i) #Schicht DICOM
        # print(z) #Schicht Cube
        z -= 1

    seg = cube
    img = patient_pixels

    visualisierung_mask(img, seg) # 3D Visualization

    # convert to float32
    img = img.astype(np.float32)
    seg = seg.astype(np.float32)

    # Numpy -> Torch
    img = torch.from_numpy(img)
    img = img.to(torch.float16)
    seg = torch.from_numpy(seg)
    seg = seg.to(torch.float16)

    # Speichern
    path = "/home/wolfda/Data/Cathi_Hoden/Test.pt"
    torch.save({"vol": img, "seg": seg, "class": "Rezidiv", "ID": "123"}, path)


if __name__ == '__main__':
    main()