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
readdata, header = nrrd.read("//media/wolfda/RAD_KI_1/Weig_CLL_9_2022/0000240614/Befundverlauf 1/0/Follow-Up 1/1.2.840.113704.1.111.10156.1531389867.6_NT01 Milz_generic_primary_primary_3508914.nrrd")
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