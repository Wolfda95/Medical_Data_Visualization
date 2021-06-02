# ----------packages------------------------------
import os
import numpy as np
import torch

from batchviewer import view_batch  # 3D Visualisierung (aus Git runtergeladen)

import pydicom  # DICOM Images (.dicom)

import nibabel as nib #NIFTI Images (.nii)

import scipy # rezize: zoom
import torchvision.transforms as transforms # rezize: torch



# -------------------Load DICOM Image------------------------------
def load_scan(path):
    slices = [pydicom.dcmread(path + '/' + s) for s in os.listdir(path)] #holt alle DICOM Dateien aus dem Ordner
    slices = [s for s in slices if 'SliceLocation' in s]
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

    patient_pixels = np.transpose(patient_pixels, (0, 2, 1))
    width = patient_pixels.shape[1]
    hight = patient_pixels.shape[2]
    view_batch(patient_pixels, width=512, height=512)

# ------------------- DICOM Header der ersten Schicht + Visualisierung (mit Maske)--------------------------------------------
def visualisierung_mask(patient_dicom, patient_pixels, img_mask):
    print(patient_dicom[1]) # DICOM Header der ersten Schicht

    patient_pixels = np.transpose(patient_pixels, (0, 2, 1))
    width = patient_pixels.shape[1]
    hight = patient_pixels.shape[2]
    view_batch(patient_pixels, img_mask, width=width, height=hight)

#############################################################################################################

# ------------------- DICOM CT BatchViwer --------------------------------------------
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
    patient_pixels = get_pixels_hu(patient_dicom)  # Numpy Array (Anzahl Schichten, x,y)
    patient_pixels = win_scale(patient_pixels, wl, ww, type(patient_pixels), [patient_pixels.min(), patient_pixels.max()])  # Numpy Array Korrigiert
    patient_pixels = patient_pixels[::-1,...]  # läuft die Schichten von hinten durch, da irgendwie die Schichten umgedreht wurden

    visualisierung(patient_dicom, patient_pixels)

# ------------------- DICOM CT BatchViwer + resize --------------------------------------------
def run_ct_resize (path, body_part):

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
    patient_pixels = get_pixels_hu(patient_dicom)  # Numpy Array (Anzahl Schichten, x,y)
    patient_pixels = win_scale(patient_pixels, wl, ww, type(patient_pixels), [patient_pixels.min(), patient_pixels.max()])  # Numpy Array Korrigiert
    patient_pixels = patient_pixels[::-1,...]  # läuft die Schichten von hinten durch, da irgendwie die Schichten umgedreht wurden
    patient_pixels = min_max_normalization(patient_pixels, 0.001) # Braucht man nicht unbedingt


    # RESIZE:

    patient_pixels = patient_pixels.astype(np.float32) # sonst meckert zoom

    # MÖGL1: Torch grid (Error)
    # pixel_torch = torch.from_numpy(patient_pixels)
    # pixel_torch = pixel_torch.to(torch.float16)
    # pixel_torch = torch.unsqueeze(pixel_torch, 0)
    # d = torch.linspace(-1, 1, 2)
    # h = torch.linspace(-1, 1, 3)
    # w = torch.linspace(-1, 1, 4)
    # meshz, meshy, meshx = torch.meshgrid((d, h, w))
    # grid = torch.stack((meshx, meshy, meshz), 3)
    # grid = grid.unsqueeze(0)  # add batch dim
    # resize = torch.nn.functional.grid_sample(pixel_torch.float(), grid, align_corners=True)

    # MÖGL2: Torch interpolate
    # pixel_torch = torch.from_numpy(patient_pixels)
    # pixel_torch = pixel_torch.to(torch.float16)
    # pixel_torch = torch.unsqueeze(pixel_torch, 0)
    # pixel_torch = torch.unsqueeze(pixel_torch, 0)
    # resize = torch.nn.functional.interpolate(pixel_torch.float(), size=[48,256,256], scale_factor=None, mode='nearest', align_corners=None, recompute_scale_factor=None)
    # resize = resize[0,0,:,:,:]

    # MÖGL3: Zoom
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.zoom.html#scipy.ndimage.zoom
    # reflect’, ‘constant’, ‘nearest’, ‘mirror’, ‘wrap’
    resize = scipy.ndimage.zoom(patient_pixels, (min(1,(48 / patient_pixels.shape[0])), (256/patient_pixels.shape[1]), (256/patient_pixels.shape[2])), mode="constant", grid_mode=True)

    print(patient_pixels.shape, resize.shape)
    visualisierung(patient_dicom, resize)

# ------------------- DICOM CT BatchViwer + Nifti Maske --------------------------------------------
def run_ct_mask (ct, body_part, mask):

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


    patient_dicom = load_scan(ct) # Load CT Bild
    patient_pixels = get_pixels_hu(patient_dicom)  # Numpy Array (Anzahl Schichten, x,y)
    patient_pixels = win_scale(patient_pixels, wl, ww, type(patient_pixels), [patient_pixels.min(), patient_pixels.max()])  # Numpy Array Korrigiert
    patient_pixels= patient_pixels[::-1, ...] # läuft die Schichten von hinten durch, da irgendwie die Schichten umgedreht wurden


    nifti_mask = nib.load(mask) # Load Maske
    img_mask = nifti_mask.get_fdata()  # Numpy Array (x,y, Anzahl Schichten)
    img_mask = img_mask.transpose(2, 0, 1)

    visualisierung_mask(patient_dicom, patient_pixels, img_mask)


# ------------------- DICOM MRT BatchViwer --------------------------------------------
def run_mrt (path):

    patient_dicom = load_scan(path)
    patient_pixels = get_pixels_hu(patient_dicom)  # Numpy Array (Anzahl Schichten, x,y)
    patient_pixels = patient_pixels[::-1,...]  # läuft die Schichten von hinten durch, da irgendwie die Schichten umgedreht wurden
    visualisierung(patient_dicom, patient_pixels)

# ------------------- DICOM MRT BatchViwer + resize--------------------------------------------
def run_mrt_resize (path):

    patient_dicom = load_scan(path)
    patient_pixels = get_pixels_hu(patient_dicom)  # Numpy Array (Anzahl Schichten, x,y)
    patient_pixels = patient_pixels[::-1,...]  # läuft die Schichten von hinten durch, da irgendwie die Schichten umgedreht wurden

    # RESIZE:

    patient_pixels = patient_pixels.astype(np.float32)  # sonst meckert zoom

    # MÖGL1: Torch grid (Error)
    # pixel_torch = torch.from_numpy(patient_pixels)
    # pixel_torch = pixel_torch.to(torch.float16)
    # pixel_torch = torch.unsqueeze(pixel_torch, 0)
    # d = torch.linspace(-1, 1, 2)
    # h = torch.linspace(-1, 1, 3)
    # w = torch.linspace(-1, 1, 4)
    # meshz, meshy, meshx = torch.meshgrid((d, h, w))
    # grid = torch.stack((meshx, meshy, meshz), 3)
    # grid = grid.unsqueeze(0)  # add batch dim
    # resize = torch.nn.functional.grid_sample(pixel_torch.float(), grid, align_corners=True)

    # MÖGL2: Torch interpolate
    # pixel_torch = torch.from_numpy(patient_pixels)
    # pixel_torch = pixel_torch.to(torch.float16)
    # pixel_torch = torch.unsqueeze(pixel_torch, 0)
    # pixel_torch = torch.unsqueeze(pixel_torch, 0)
    # resize = torch.nn.functional.interpolate(pixel_torch.float(), size=[48,256,256], scale_factor=None, mode='nearest', align_corners=None, recompute_scale_factor=None)
    # resize = resize[0,0,:,:,:]

    # MÖGL3: Zoom
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.zoom.html#scipy.ndimage.zoom
    # reflect’, ‘constant’, ‘nearest’, ‘mirror’, ‘wrap’
    resize = scipy.ndimage.zoom(patient_pixels, min(1,
    (48 / patient_pixels.shape[0]), (256 / patient_pixels.shape[1]), (256 / patient_pixels.shape[2])), mode="constant",
                                grid_mode=True)

    print(patient_pixels.shape, resize.shape)
    visualisierung(patient_dicom, resize)

# ------------------- DICOM MRT BatchViwer + Nifti Maske--------------------------------------------
def run_mrt_mask (ct, mask):

    patient_dicom = load_scan(ct) # load ct Bild
    patient_pixels = get_pixels_hu(patient_dicom)  # Numpy Array (Anzahl Schichten, x,y)
    patient_pixels = patient_pixels[::-1,...]  # läuft die Schichten von hinten durch, da irgendwie die Schichten umgedreht wurden

    nifti_mask = nib.load(mask) # load Maske
    img_mask = nifti_mask.get_fdata()  # Numpy Array (x,y, Anzahl Schichten)
    img_mask = img_mask.transpose(2, 0, 1)

    visualisierung_mask(patient_dicom, patient_pixels, img_mask)



