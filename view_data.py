# -*- coding: utf-8 -*-

import os
import numpy as np
import torch
import copy
from math import *
import matplotlib.pyplot as plt
from functools import reduce

# =============================================================================
# NIFTI Image:
# =============================================================================
r"""import nibabel as nib #NIFTI Images (.nii)
from batchviewer import view_batch # aus Git runtergeladen
file_path = "/home/wolfda/data/MUSTERMANN,MAXIMILAN_1000003010000030_1_59/RoiVolume/R1.uint16.nii.gz" #r"C:\Users\sup.alexisa\Downloads\Task02_Heart\Task02_Heart\imagesTr\la_005.nii.gz"
img = nib.load(file_path)
print(img.shape)
print(img.header)
img = img.get_fdata()
img = img.transpose(2, 0, 1)
print(img.shape)
view_batch(img, width=1000, height=1000)
"""

# =============================================================================
# DICOM Image Mögl1: (Ein Bild bestehend aus mehreren Schichten + Tolle Visualisiereung + Speicherung)
# =============================================================================
# ----------packages------------------------------
from batchviewer import view_batch  # aus Git runtergeladen

# reading in dicom files
import pydicom  # DICOM Images (.dicom)

# skimage image processing packages
from skimage import measure, morphology
from skimage.morphology import ball, binary_closing
from skimage.measure import label, regionprops

# scipy linear algebra functions 
from scipy.linalg import norm
import scipy.ndimage

# plotly 3D interactive graphs 
import plotly  # conda install -c plotly plotly=4.12.0
from plotly.graph_objs import *
import chart_studio.plotly as py


# set plotly credentials here
# this allows you to send results to your account 
# plotly.tools.set_credentials_file(username=your_username, api_key=your_key)

# -------------------Load Image------------------------------
def load_scan(path):  # DICOM Bild einlesen
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


# extract DICOM pixels for each slice location
path = '/media/wolfda/diskAshur2/0008284111_pet_corrected/3783923/3'  # Path von einem DICOM Bild (ein Ordner mit 88 DICOM Dateien)
# path = 'C:\Dixon_example_dicom'
patient_dicom = load_scan(path)
patient_pixels = get_pixels_hu(patient_dicom)  # bekommen Numpy Array

# ----Visualization-------------------------------------------------
# display a single slice
print(patient_dicom)
plt.imshow(patient_pixels[5], cmap=plt.cm.bone)  # [5] ist die Schischt die angezeit wird

# display interactive
patient_pixels = np.transpose(patient_pixels, (0, 2, 1))
print(patient_pixels.shape)
view_batch(patient_pixels, width=384, height=312)

"""
#----save---------------------------------------------------------
def save(args, mask, name, i, image):
    save_folder = args

    print(image.shape, name)

    image = torch.from_numpy(image)
    mask = torch.from_numpy(mask)

    image = image.to(torch.float16)
    image = image.unsqueeze(0)

    mask = mask.to(torch.int16)
    path = save_folder + "/" + str(i) + ".pt"
    torch.save({"vol": image, "mask": mask, "id": name.split(".")[0]}, path)
    
mask = np.array([1,2,3])    
save("/home/wolfda/PPA_output_20201202171019/Mustermann_Maximilan/",mask ,"Test", "FileName", patient_pixels)

data = torch.load('/home/wolfda/PPA_output_20201202171019/Mustermann_Maximilan/FileName.pt')
print(data)


# ipywidgets interactive plots (geht nur in Jupyter)
#from ipywidgets.widgets import * 
#import ipywidgets as widgets
#plt.figure(1)
#def dicom_animation(x):
#    plt.imshow(patient_pixels[x])
#    return x
#interact(dicom_animation, x=(0, len(patient_pixels)-1))"""

# =============================================================================
# DICOM Image Mögl2: (nur eine Schicht von einem Bild)
# =============================================================================
"""import pydicom as dicom  # DICOM Images (.dicom)

# Nur ein Bild der Serie einlesen:
# dataset = dicom.read_file('C:\\DICOM_Test_Bild\\Bilder1\\FB_umap_4States_Acc0.4_F_112\\1.2.840.113654.2.70.1.102853707388696908138401463515242578675.dcm') # an Name .dcm anhängen UND \\ statt \
dataset = dicom.read_file("/home/wolfda/PPA_output_20201202171019/Mustermann_Maximilan/59_Abd_ep2d_diff_b50_800_tra_ADC_DFC_MIX/00000035.dcm")

print(dataset)
print(dataset.pixel_array.shape)
print(dataset.Rows)
print(dataset.Columns)

plt.imshow(dataset.pixel_array, plt.cm.bone)
plt.show()
"""
# =============================================================================
# DICOM Image Mögl3: (Ein Bild bestehend aus mehreren Schichten + Pixel reduzierung)
# =============================================================================
"""import pydicom as dicom #DICOM Images (.dicom)
import pandas as pd

path = '/home/wolfda/PPA_output_20201202171019/Mustermann_Maximilan/15_Abd_MRAC_CAIPI_HiRes_opp' #Path von einem DICOM Bild (ein Ordner mit 88 DICOM Dateien)
slices = [dicom.read_file(path + "/" + s) for s in os.listdir(path)] #holt alle DICOM Dateien aus dem Ordner
slices.sort(key = lambda x: int(x.ImagePositionPatient[2])) #ImagePositionPatient[2] sagt an welcher Stelle die DICOM Datei kommen muss

print(len(slices)) # Anzahl an Schichten
print(slices[0]) # Alle Infos zur ersten Schicht 
print(slices[0].pixel_array.shape) #Pixelarray von der ersten Schicht (Ist eine Liste, für Numpy: np.array(each_slice.pixel_array))

plt.imshow(slices[0].pixel_array, plt.cm.bone) 
plt.show() # Plot von erster Schicht. 

#-----------Pixelgröße der einzelnen Schichten verkleinern (auf 150 Pixel)-----------------------------

import cv2
IMG_PX_SIZE = 150
fig = plt.figure()
for num,each_slice in enumerate(slices[:12]): #durchläuft nue die ersten 12 Schichten
    y = fig.add_subplot(3,4,num+1)
    new_img = cv2.resize(np.array(each_slice.pixel_array),(IMG_PX_SIZE,IMG_PX_SIZE)) #(Numpy Array der geändert werden soll, (150,150) neue Pixelgröße)
    y.imshow(new_img,plt.cm.bone)
plt.show()
print(new_img.shape)"""

# =============================================================================
# DICOM Image Mögl4: (Mehrere Bilder (=mehrer Patienten) betehend jeweils aus mehrern Schichten + Pixel reduziereung)
# =============================================================================
"""import pydicom as dicom #DICOM Images (.dcm)
import pandas as pd
import cv2

path_out = '/home/wolfda/PPA_output_20201202171019/Mustermann_Maximilan' #Ordner mit vielen DICOM Ordnern (vielen Patienten)
patients = os.listdir(path_out) #Liste mit den Pathes der DICOM Ordnern (Patienten)

for patient in patients[:5]: #durchläuft die Liste (Hier: 5 Patienten)
    path = path_out + "/" + patient #Path für einen DICOM Ordner (Einen Patienten) (Enthält viele DICOM Dateien - 3D Bild)
    slices = [dicom.read_file(path + "/" + s) for s in os.listdir(path)] #holt alle DICOM Dateien aus dem DICOM Ordner (os.listdir(path) enthält die Pathes für alle einzlenen DICOM Files von dem einen DICOM Ordner (von dem einen Patient))
    slices.sort(key = lambda x: int(x.ImagePositionPatient[2])) #ImagePositionPatient[2] sagt an welcher Stelle die DICOM Datei kommen muss -> Wird sortiert
    print(len(slices)) # Anzahl an Schichten
    #print(slices[0]) # Alle Infos zur ersten Schicht 
    print(slices[0].pixel_array.shape) #Pixelarray von der ersten Schicht (Ist eine Liste, für Numpy: np.array(each_slice.pixel_array))
    plt.imshow(slices[0].pixel_array, plt.cm.bone)  # Plot von erster Schicht. 
    
    #-----------Pixelgröße der einzelnen Schichten verkleinern (auf 150 Pixel)-----------------------------
    IMG_PX_SIZE = 150
    fig = plt.figure()
    for num,each_slice in enumerate(slices[:12]): #durchläuft nur die ersten 12 Schichten
        y = fig.add_subplot(3,4,num+1)
        new_img = cv2.resize(np.array(each_slice.pixel_array),(IMG_PX_SIZE,IMG_PX_SIZE)) #(Numpy Array der geändert werden soll, (150,150) neue Pixelgröße)
        y.imshow(new_img, plt.cm.bone)
    plt.show()
    print(new_img.shape)"""

# =============================================================================
# DICOM to NIFTI: (Funktioniert :-) ) -->Bilder mit fiji öffnen
# =============================================================================    
"""import dicom2nifti # pip install dicom2nifti

dicom2nifti.convert_directory('/home/wolfda/PPA_output_20201202171019/Mustermann_Maximilan/59_Abd_ep2d_diff_b50_800_tra_ADC_DFC_MIX', '/home/wolfda/PPA_output_20201202171019/Mustermann_Maximilan/Nifti' ) # erzeugt .nii.gz Datei"""

# =============================================================================
# DICOM to PNG:
# =============================================================================
"""import cv2
import os
import pydicom

inputdir = 'C:\DICOM_Test_Bild\Bilder1\WB_WIP996_MRAC_CAIPI_HiRes_in_COMP_PT_34'
outdir = 'C:\DICOM_Test_Bild\Bilder1\PNG_Bilder'
#os.mkdir(outdir)

test_list = [ f for f in  os.listdir(inputdir)]

for f in test_list:   
    ds = pydicom.read_file(inputdir + "\\" + f) # read dicom image
    img = ds.pixel_array # get image array
    cv2.imwrite(outdir + f.replace('.dcm','.png'),img) # write png image"""

# =============================================================================
# DICOM to PNG:
# =============================================================================
"""import numpy as np
from PIL import Image
import os
import pydicom

inputdir = 'C:\DICOM_Test_Bild\Bilder1\WB_WIP996_MRAC_CAIPI_HiRes_in_COMP_PT_34'
outdir = 'C:\DICOM_Test_Bild\Bilder1\PNG_Bilder'

test_list = [ f for f in  os.listdir(inputdir)]
for f in test_list:   
    ds = pydicom.read_file(inputdir + "\\" + f) # read dicom image
    img = ds.pixel_array # get image array
    print(img[200,200])
    img2 = np.asarray(img)
    img3 = Image.fromarray(img2)
    img3.save(outdir + 'testrgb' + f + '.png')"""
