import numpy as np

import nibabel as nib #NIFTI Images (.nii)
from batchviewer import view_batch # aus Git runtergeladen

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


#######################################################################################################################

def nifti_ct(path, body_part):
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


    nifti = nib.load(path)
    img = nifti.get_fdata()  # Numpy Array (x,y, Anzahl Schichten)
    img = win_scale(img, wl, ww, type(img),[img.min(), img.max()])  # Numpy Array Korrigiert

    print(nifti.header)

    img = img.transpose(2, 0, 1)
    width = img.shape[1]
    hight = img.shape[2]
    view_batch(img, width=width, height=hight)



def nifti_ct_mask(ct, body_part, mask):
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

    nifti_ct = nib.load(ct)
    img_ct = nifti_ct.get_fdata()  # Numpy Array (x,y, Anzahl Schichten)
    img_ct = win_scale(img_ct, wl, ww, type(img_ct), [img_ct.min(), img_ct.max()])  # Numpy Array Korrigiert
    img_ct = img_ct.transpose(2, 0, 1)
    print(nifti_ct.header)

    nifti_mask = nib.load(mask)
    img_mask = nifti_mask.get_fdata()  # Numpy Array (x,y, Anzahl Schichten)
    img_mask = img_mask.transpose(2, 0, 1)

    width = img_ct.shape[1]
    hight = img_ct.shape[2]
    view_batch(img_ct,img_mask, width=width, height=hight)






def nifti_mrt(path):

    nifti = nib.load(path)
    img = nifti.get_fdata() # Numpy Array (x,y, Anzahl Schichten)

    print(nifti.header)
    print(img.shape)

    img = img.transpose(2, 0, 1)
    width = img.shape[1]
    hight = img.shape[2]
    view_batch(img, width=width, height=hight)


def nifti_mrt_mask(mrt, mask):

    nifti_mrt = nib.load(mrt)
    img_mrt = nifti_mrt.get_fdata() # Numpy Array (x,y, Anzahl Schichten)
    img_mrt = img_mrt.transpose(2, 0, 1)
    print(nifti_mrt.header)

    nifti_mask = nib.load(mask)
    img_mask = nifti_mask.get_fdata()  # Numpy Array (x,y, Anzahl Schichten)
    img_mask = img_mask.transpose(2, 0, 1)

    width = img_mrt.shape[1]
    hight = img_mrt.shape[2]
    view_batch(img_mrt,img_mask, width=width, height=hight)