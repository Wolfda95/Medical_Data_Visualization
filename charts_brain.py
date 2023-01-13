import matplotlib.pyplot as plt
import numpy as np

######################################################################################################################
# ACC AutoPET
# Höher der Bars (=Ergbnisse)
hight = [59.64
,62.76
, 71.414
, 71.034
, 79.31
, 72.892
, 75.93
]

# Namen der Bars
names = ['Scratch', 'All', "Every-n", 'HashAll', 'Hash', 'SSIM', 'Mutal' ]
x_pos = np.arange(len(names))

#plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [03.4022786
, 6.0334956
, 2.27
, 3.2078373
, 01.9918584
, 2.4351413,
1.563099
]

# x-Achse
plt.ylim(50,85)

# X-Lable
plt.ylabel('Accuracy in %')

plt.title('PreTrain with AutoPET Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray', "orange", 'darkorange', 'darkorange', 'darkorange', 'darkorange'], yerr=yer, capsize=7)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/Cathi/Plots/ACC_AutoPET_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Cathi/Plots/ACC_AutoPET_image.png", format="png")
plt.savefig("/home/wolfda/Data/Cathi/Plots/ACC_AutoPET_pdf.pdf", format="pdf")

plt.show()

######################################################################################################################
# AUC AutoPET
# Höher der Bars (=Ergbnisse)
hight = [67.81
, 72.66
, 79.524
, 78.73
, 83.18
, 79.92
, 76.00
]

# Namen der Bars
names = ['Scratch', 'All', "Every-n", 'HashAll', 'Hash', 'SSIM', 'Mutal' ]
x_pos = np.arange(len(names))

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [03.7779756

, 1.28831021
, 2.29
, 02.7996047

, 2.7578462

, 01.5231262

, 1.0585745

]

# x-Achse
plt.ylim(60,90)

# X-Lable
plt.ylabel('AUC in %')

plt.title('PreTrain with AutoPET Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width,  color=['gray', 'gray', "orange", 'darkorange', 'darkorange', 'darkorange', 'darkorange'], yerr=yer, capsize=7,)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/Cathi/Plots/AUC_AutoPET_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Cathi/Plots/AUC_AutoPET_image.png", format="png")
plt.savefig("/home/wolfda/Data/Cathi/Plots/AUC_AutoPET_pdf.pdf", format="pdf")

plt.show()
#
# ######################################################################################################################
# F1 AutoPET
# Höher der Bars (=Ergbnisse)
hight = [44.716

, 53.45
, 68.738
, 69.2

, 76.494

, 67.844

, 72.228

]

# Namen der Bars
names = ['Scratch', 'All', "Every-n", 'HashAll', 'Hash', 'SSIM', 'Mutal' ]
x_pos = np.arange(len(names))

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [7.7393579

, 07.2989588
, 1.424
, 2.0662204

, 2.4283575

, 3.1945871

, 1.0592985

]

# x-Achse
plt.ylim(30,90)

# X-Lable
plt.ylabel('F1 in %')

plt.title('PreTrain with AutoPET Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray', "orange", 'darkorange', 'darkorange', 'darkorange', 'darkorange'], yerr=yer, capsize=7,)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/Cathi/Plots/F1_AutoPET_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Cathi/Plots/F1_AutoPET_image.png", format="png")
plt.savefig("/home/wolfda/Data/Cathi/Plots/F1_AutoPET_pdf.pdf", format="pdf")

plt.show()
#

#####################################################################################################################
# ACC LIDC
# Höher der Bars (=Ergbnisse)
hight = [59.64

, 68.126
, 75.07
, 78.842

, 80.68

, 78.322

, 78.322
]

# Namen der Bars
names = ['Scratch', 'All', 'Every-n', 'HashAll', 'Hash', 'SSIM', 'Mutal' ]
x_pos = np.arange(len(names))

#plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [3.4022786
, 05.8788111
, 2.35


, 01.8544472


, 3.2243346


,4.6000884


, 03.6728055


]

# x-Achse
plt.ylim(50,85)

# X-Lable
plt.ylabel('Accuracy in %')

plt.title('PreTrain with LIDC Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray', 'orange', 'darkorange', 'darkorange', 'darkorange', 'darkorange'], yerr=yer, capsize=7)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/Cathi/Plots/Acc_LIDC_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Cathi/Plots/Acc_LIDC_image.png", format="png")
plt.savefig("/home/wolfda/Data/Cathi/Plots/Acc_LIDC_pdf.pdf", format="pdf")

plt.show()

######################################################################################################################
# AUC LIDC
# Höher der Bars (=Ergbnisse)
hight = [67.81

, 73.428
, 82.71


, 86.762



, 84.064



, 85.904



, 80.156



]

# Namen der Bars
names = ['Scratch', 'All', "Every-n", 'HashAll', 'Hash', 'SSIM', 'Mutal' ]
x_pos = np.arange(len(names))

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [3.7779756



,4.661986

, 1.67
,1.7039797


, 1.6853051


, 1.3626396


, 3.1033616

]

# x-Achse
plt.ylim(60,90)

# X-Lable
plt.ylabel('AUC in %')

plt.title('PreTrain with LIDC Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width,  color=['gray', 'gray', "orange", 'darkorange', 'darkorange', 'darkorange', 'darkorange'], yerr=yer, capsize=7,)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/Cathi/Plots/AUC_LIDC_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Cathi/Plots/AUC_LIDC_image.png", format="png")
plt.savefig("/home/wolfda/Data/Cathi/Plots/AUC_LIDC_pdf.pdf", format="pdf")

plt.show()
#
# ######################################################################################################################
# F1 LIDC
# Höher der Bars (=Ergbnisse)
hight = [
44.716

, 60.91

, 73.988

, 76.608



, 80.02




,75.68

, 70.604


]

# Namen der Bars
names = ['Scratch', 'All', "Every-n", 'HashAll', 'Hash', 'SSIM', 'Mutal' ]
x_pos = np.arange(len(names))

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [7.7393579


,7.1802716
, 2.662

, 02.2906797

,2.9715372


,05.8195733


, 5.5692268



]

# x-Achse
plt.ylim(30,90)

# X-Lable
plt.ylabel('F1 in %')

plt.title('PreTrain with LIDC Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray', "orange", 'darkorange', 'darkorange', 'darkorange', 'darkorange'], yerr=yer, capsize=7,)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)


plt.savefig("/home/wolfda/Data/Cathi/Plots/F1_LIDC_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Cathi/Plots/F1_LIDC_image.png", format="png")
plt.savefig("/home/wolfda/Data/Cathi/Plots/F1_LIDC_pdf.pdf", format="pdf")


plt.show()