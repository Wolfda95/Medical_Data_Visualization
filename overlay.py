import matplotlib.pyplot as plt
import os
import numpy as np
import torch
import nibabel as nib #NIFTI Images (.nii)


from batchviewer import view_batch  # 3D Visualisierung (aus Git runtergeladen)

import scipy.ndimage # rezize: zoom

import pydicom  # DICOM Images (.dicom)

# -------------------Load DICOM Image------------------------------
def load_scan(path):
    slices = [pydicom.dcmread(path + '/' + s) for s in sorted(os.listdir(path))] #holt alle DICOM Dateien aus dem Ordner
    #slices = [s for s in slices if 'SliceLocation' in s]
    slices.sort(key=lambda x: int(x.InstanceNumber)) #InstanceNumber sagt an welcher Stelle die DICOM Datei kommen muss !!!!!!!!!!!
    # try:
    #     slice_thickness = np.abs(slices[0].ImagePositionPatient[2] -slices[1].ImagePositionPatient[2])
    # except:
    #
    #     slice_thickness = np.abs(slices[0].SliceLocation - slices[1].SliceLocation)
    #
    # for s in slices:
    #    s.SliceThickness = slice_thickness
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

# ---------------------- Bilder überlagern + Plot ----------------------------------------------
def images(mask, img, schicht):
    mask = mask[schicht]
    img = img[schicht]
    plt.imshow(mask, cmap='jet',)
    plt.imshow(img, cmap='gray', alpha=0.5)
    plt.show()


# ------------------- Batchviewr Visualisierung (mit Maske)--------------------------------------------
def visualisierung_mask(patient_pixels, img_mask):

    patient_pixels = np.transpose(patient_pixels, (0, 2, 1))
    width = patient_pixels.shape[1]
    hight = patient_pixels.shape[2]
    view_batch(patient_pixels, img_mask, width=width, height=hight)

################################################################################################

def overlay_dicom_pytorch(img, mask, schicht):

    # PyTorch Maske
    mask = torch.load(mask) #[::-1,...] # für Torch: .permute(0, 2, 1)
    #mask = scipy.ndimage.zoom(mask, (min(1, (56 / mask.shape[0])), (120 / mask.shape[1]), (160 / mask.shape[2])),mode="grid-constant", grid_mode=True)
    print(mask.shape)

    # Dicom Image
    patient_dicom = load_scan(img)
    patient_pixels = get_pixels_hu(patient_dicom)  # Numpy Array (Anzahl Schichten, x,y)
    #patient_pixels = patient_pixels[::-1,...]  # läuft die Schichten von hinten durch, da irgendwie die Schichten umgedreht wurden
    #patient_pixels = scipy.ndimage.zoom(patient_pixels, (min(1, (56 / patient_pixels.shape[0])), (802 / patient_pixels.shape[1]), (802 / patient_pixels.shape[2])), mode="grid-constant", grid_mode=True)
    print(patient_pixels.shape)

    images(mask, patient_pixels, schicht)
    visualisierung_mask(patient_pixels, np.transpose(mask, (0, 2, 1)))

# def overlay_dicom_nifti(img, mask, schicht):
#
#     # PyTorch Maske
#     nifti = nib.load(mask)
#     mask = nifti.get_fdata()  # Numpy Array (x,y, Anzahl Schichten)
#
#     print(nifti.header)
#     print(img.shape)
#     print(mask.shape)
#
#     # Dicom Image
#     patient_dicom = load_scan(img)
#     patient_pixels = get_pixels_hu(patient_dicom)  # Numpy Array (Anzahl Schichten, x,y)
#     #patient_pixels = patient_pixels[::-1,...]  # läuft die Schichten von hinten durch, da irgendwie die Schichten umgedreht wurden
#     #patient_pixels = scipy.ndimage.zoom(patient_pixels, (min(1, (56 / patient_pixels.shape[0])), (802 / patient_pixels.shape[1]), (802 / patient_pixels.shape[2])), mode="grid-constant", grid_mode=True)
#     print(patient_pixels.shape)
#
#     images(mask, patient_pixels, schicht)
#     visualisierung_mask(patient_pixels, np.transpose(mask, (0, 2, 1)))