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
readdata, header = nrrd.read("//media/wolfda/Ashur Pro2/VC_Hoden_multi/0003027408/Befundverlauf 1/0/Baseline/1.2.840.113704.1.111.9840.1448875333.6_F01 lis_generic_primary_primary_3026345.nrrd")
print(readdata.shape)
print(header)

print(type(readdata))
#patient_pixels = readdata
patient_pixels = np.transpose(readdata, (2, 0, 1))
print(patient_pixels.shape)
width = patient_pixels.shape[1]
hight = patient_pixels.shape[2]
view_batch(patient_pixels, width=width, height=hight)

# img =readdata[1,...]
# img = img.transpose(2, 0, 1)
#print(img.shape)
#img = min_max_normalization(readdata[1,...], 0.001)
# imgplot = plt.imshow(readdata[1,...])
# plt.show()

# readdata = readdata.transpose(3, 0, 1, 2) # Anzahl Schichten muss im BatchVwer vorne Stehen (Anzahl Schichten,x,y)
# width = readdata.shape[1]
# hight = readdata.shape[2]
# view_batch(readdata, width=width, height=hight)