import numpy as np
import pydicom as dicom  # DICOM Images (.dicom)
import nibabel as nib #NIFTI Images (.nii)
from batchviewer import view_batch # aus Git runtergeladen

import scipy
from skimage import measure
from plotly.offline import iplot
from plotly.figure_factory import create_trisurf
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

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

# ------------------- Nifti CT BatchViwer --------------------------------------------
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

    img = img.transpose(2, 0, 1) # Anzahl Schichten muss im BatchVwer vorne Stehen (Anzahl Schichten,x,y)
    width = img.shape[1]
    hight = img.shape[2]
    view_batch(img, width=width, height=hight)


# ------------------- Nifti CT BatchViwer + Maske --------------------------------------------
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
    img_ct = img_ct.transpose(2, 0, 1) # Anzahl Schichten muss im BatchVwer vorne Stehen (Anzahl Schichten,x,y)
    print(nifti_ct.header)

    nifti_mask = nib.load(mask)
    img_mask = nifti_mask.get_fdata()  # Numpy Array (x,y, Anzahl Schichten)
    img_mask = img_mask.transpose(2, 0, 1) # Anzahl Schichten muss im BatchVwer vorne Stehen (Anzahl Schichten,x,y)

    width = img_ct.shape[1]
    hight = img_ct.shape[2]
    view_batch(img_ct,img_mask, width=width, height=hight)

# ------------------- Nifti MRT BatchViwer --------------------------------------------
def nifti_mrt(path):

    nifti = nib.load(path)
    img = nifti.get_fdata() # Numpy Array (x,y, Anzahl Schichten)

    print(nifti.header)
    print(img.shape)

    img = img.transpose(2, 0, 1) # Anzahl Schichten muss im BatchVwer vorne Stehen (Anzahl Schichten,x,y)
    width = img.shape[1]
    hight = img.shape[2]
    view_batch(img, width=width, height=hight)

# ------------------- Nifti MRT BatchViwer + Maske--------------------------------------------
def nifti_mrt_mask(mrt, mask):

    nifti_mrt = nib.load(mrt)
    img_mrt = nifti_mrt.get_fdata() # Numpy Array (x,y, Anzahl Schichten)
    img_mrt = img_mrt.transpose(2, 0, 1) # Anzahl Schichten muss im BatchVwer vorne Stehen (Anzahl Schichten,x,y)
    print(nifti_mrt.header)

    nifti_mask = nib.load(mask)
    img_mask = nifti_mask.get_fdata()  # Numpy Array (x,y, Anzahl Schichten)
    img_mask = img_mask.transpose(2, 0, 1) # Anzahl Schichten muss im BatchVwer vorne Stehen (Anzahl Schichten,x,y)

    width = img_mrt.shape[1]
    hight = img_mrt.shape[2]
    view_batch(img_mrt,img_mask, width=width, height=hight)


# ------------------- Nifti Volume --------------------------------------------
def nifti_volume(mask, image):

    # Nifti Mask
    nifti_mask = nib.load(mask)
    mask = nifti_mask.get_fdata() # Numpy Array (x,y, Anzahl Schichten)
    mask = mask.transpose(2, 0, 1)  # Anzahl Schichten muss orne Stehen (Anzahl Schichten,x,y)
    print(mask.shape)

    # Dicom Bild (brauche nur den Header)
    dataset = dicom.read_file(image)
    spacing = np.array([float(dataset.SliceThickness), float(dataset.PixelSpacing[0]), float(dataset.PixelSpacing[0])])
    resize_factor = spacing / [1,1,1]
    new_real_shape = mask.shape * resize_factor
    new_shape = np.round(new_real_shape)
    real_resize_factor = new_shape / mask.shape
    new_spacing = spacing / real_resize_factor
    new_mask = scipy.ndimage.interpolation.zoom(mask, real_resize_factor, prefilter=False, mode='nearest', cval=0.0) # prefilter=False Sonst ist das Bild weiß auf schichten die keine Segmentierung haben
    print(new_mask.shape)

    # Smoothing
    #https://docs.scipy.org/doc/scipy/reference/reference/generated/scipy.ndimage.gaussian_filter.html#scipy.ndimage.gaussian_filter
    new_mask = scipy.ndimage.gaussian_filter(new_mask, sigma=[1,1,1], order=0, output=None, mode='reflect', cval=0.0, truncate=4.0)

    # Was komisches
    p = new_mask.transpose(2, 1, 0)

    print("Calculating surface")
    verts, faces, norm, val = measure.marching_cubes_lewiner(p, step_size=1, allow_degenerate=True)

    # Plot Mögl.1
    x, y, z = zip(*verts)

    print("Drawing 1")

    # colormap=['rgb(255,105,180)','rgb(255,255,51)','rgb(0,191,255)']
    colormap = ['rgb(236, 236, 212)', 'rgb(236, 236, 212)']
    #colormap = ['rgb(50,205,50)', 'rgb(50,205,50)'] # Farbe des Dings anpassen

    fig = create_trisurf(x=x, y=y, z=z, plot_edges=False,
                            show_colorbar = False, # Brauchen keine Colorbar weil nur eine Farbe
                            colormap=colormap,
                            simplices=faces,
                            showbackground = True,
                            backgroundcolor='rgb(64, 64, 64)', # Hintergrund Farbe Anpassen
                            title="Lymphom") # Titel anpassen
    iplot(fig)

    # # Plot Mögl. 2
    # print("Drawing 2")
    # x, y, z = zip(*verts)
    # fig = plt.figure(figsize=(10, 10))
    # ax = fig.add_subplot(111, projection='3d')
    #
    # # Fancy indexing: `verts[faces]` to generate a collection of triangles
    # mesh = Poly3DCollection(verts[faces], linewidths=0.05, alpha=1)
    # face_color = [1, 1, 0.9]
    # mesh.set_facecolor(face_color)
    # ax.add_collection3d(mesh)
    #
    # ax.set_xlim(0, max(x))
    # ax.set_ylim(0, max(y))
    # ax.set_zlim(0, max(z))
    # #     ax.set_axis_bgcolor((0.7, 0.7, 0.7))
    # ax.set_facecolor((0.7, 0.7, 0.7))
    # plt.show()



    #values = np.unique(new_mask)
    #print(values)

    width = mask.shape[1]
    hight = mask.shape[2]
    view_batch(new_mask, width=width, height=hight)