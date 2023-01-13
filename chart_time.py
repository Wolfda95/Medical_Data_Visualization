import matplotlib.pyplot as plt
import numpy as np

######################################################################################################################
# AutoPET PreTrain
# Höher der Bars (=Ergbnisse)
hight = [0
, 538
, 57
, 57, 62, 204
]

# Namen der Bars
names = ['Scratch', 'All',"Every-n", 'Hash', 'SSIM', "Muatl"]
x_pos = np.arange(len(names))

#plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]


# x-Achse
plt.ylim(0,600)

# X-Lable
plt.ylabel('Time in Hour')

plt.title('AutoPET')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray', "orange", 'darkorange', 'darkorange', 'darkorange'], capsize=7)
plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/PreTrain_AutoPET_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/PreTrain_AutoPET_image.png", format="png")
plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/PreTrain_AutoPET_pdf.pdf", format="pdf")

plt.show()

######################################################################################################################
# LIDC PreTrain
# Höher der Bars (=Ergbnisse)
hight = [0, 280
, 27
, 27
, 34, 194
]

# Namen der Bars
names = ['Scratch', 'All',"Every-n", 'Hash', 'SSIM', "Muatl"]
x_pos = np.arange(len(names))

#plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]


# x-Achse
plt.ylim(0,600)

# X-Lable
plt.ylabel('Time in Hour')

plt.title('LIDC')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray', "orange", 'darkorange', 'darkorange', 'darkorange'], capsize=7)
plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/PreTrain_LIDC_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/PreTrain_LIDC_image.png", format="png")
plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/PreTrain_LIDC_pdf.pdf", format="pdf")

plt.show()

######################################################################################################################
# Similarity AutoPET
# Höher der Bars (=Ergbnisse)
hight = [0, 0.4
, 20
, 240
, 14400
]

# Namen der Bars
names = ['All',"Every-n", 'Hash', 'SSIM', "Muatl"]
x_pos = np.arange(len(names))

#plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5]


# x-Achse
plt.ylim(0,20000)

# X-Lable
plt.ylabel('Time in minutes')

plt.title('AutoPET')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width, color=['gray', "orange", 'darkorange', 'darkorange', 'darkorange'], capsize=7)
plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/Similarity_AutoPET_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/Similarity_AutoPET_image.png", format="png")
plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/Similarity_AutoPET_pdf.pdf", format="pdf")

plt.show()


######################################################################################################################
# Similarity LIDC
# Höher der Bars (=Ergbnisse)
hight = [0, 0.1
, 10
, 120
, 360
]

# Namen der Bars
names = ['All',"Every-n", 'Hash', 'SSIM', "Muatl"]
x_pos = np.arange(len(names))

#plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5]


# x-Achse
plt.ylim(0,500)

# X-Lable
plt.ylabel('Time in minutes')

plt.title('LIDC')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width, color=['gray', "orange", 'darkorange', 'darkorange', 'darkorange'], capsize=7)
plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/Similarity_LIDC_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/Similarity_LIDC_image.png", format="png")
plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/Similarity_LIDC_pdf.pdf", format="pdf")

plt.show()

