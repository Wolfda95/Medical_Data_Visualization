# ----------packages------------------------------
import os
import numpy as np
import torch

from batchviewer import view_batch  # aus Git runtergeladen

import pydicom  # DICOM Images (.dicom)


# -------------------Load DICOM Image------------------------------
def load_scan(path):
    slices = [pydicom.dcmread(path + '/' + s) for s in
              os.listdir(path)]
    slices = [s for s in slices if 'SliceLocation' in s]
    slices.sort(key=lambda x: int(x.InstanceNumber))
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

    # Convert to Hounsfield units (HU)
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



# ------------------- DICOM Header der ersten Schicht + Visualisierung --------------------------------------------
def visualisierung(patient_dicom, patient_pixels):
    print(patient_dicom[1]) # DICOM Header der ersten Schicht

    patient_pixels = np.transpose(patient_pixels, (0, 2, 1))
    width = patient_pixels.shape[1]
    hight = patient_pixels.shape[2]
    view_batch(patient_pixels, width=width, height=hight)


#############################################################################################################

def run_ct (path, body_part):

    if body_part == "abdomen":
        wl = 60
        ww = 400
    if body_part == "angio":
        wl = 300
        ww = 600
    if body_part == "bone":
        wl = 300
        ww = 150
    if body_part == "brain":
        wl = 40
        ww = 80
    if body_part == "chest":
        wl = 40
        ww = 400
    if body_part == "lungs":
        wl = -400
        ww = 1500
    else:
        print("not a correct body_part")


    patient_dicom = load_scan(path)
    patient_pixels = get_pixels_hu(patient_dicom)  # bekommen Numpy Array
    patient_pixels = win_scale(patient_pixels, wl, ww, type(patient_pixels), [patient_pixels.min(), patient_pixels.max()])  # Bekommt Numpy Array Korrigiert
    visualisierung(patient_dicom, patient_pixels)


def run_mrt (path):

    patient_dicom = load_scan(path)
    patient_pixels = get_pixels_hu(patient_dicom)  # bekommen Numpy Array
    visualisierung(patient_dicom, patient_pixels)




