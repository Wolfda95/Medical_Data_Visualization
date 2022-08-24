import numpy as np
import nrrd
from batchviewer import view_batch # aus Git runtergeladen
import matplotlib.pyplot as plt

def min_max_normalization(data, eps):
    mn = data.min()
    mx = data.max()
    data_normalized = data - mn
    old_range = mx - mn + eps
    data_normalized /= old_range

    return data_normalized

# Read the data back from file
readdata, header = nrrd.read("/home/wolfda/Downloads/test_registration_cut_rgb.nrrd")
print(readdata.shape)
print(header)

img =readdata[1,...]
img = img.transpose(2, 0, 1)
print(img.shape)
#img = min_max_normalization(readdata[1,...], 0.001)
imgplot = plt.imshow(readdata[1,...])
plt.show()

# readdata = readdata.transpose(3, 0, 1, 2) # Anzahl Schichten muss im BatchVwer vorne Stehen (Anzahl Schichten,x,y)
# width = readdata.shape[1]
# hight = readdata.shape[2]
# view_batch(readdata, width=width, height=hight)