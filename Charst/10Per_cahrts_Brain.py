import matplotlib.pyplot as plt
import numpy as np

######################################################################################################################
# ACC AutoPET
# Höher der Bars (=Ergbnisse)
hight = [59.64,
62.76
, 73.79
, 73.79
]

# Namen der Bars
names = ['Scratch', 'All', 'Everyn', 'Hash' ]
x_pos = np.arange(len(names))

#plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [3.4022786

, 03.0334956

,03.7106702

,02.5195238

]

# x-Achse
plt.ylim(50,80)

# X-Lable
plt.ylabel('Accuracy in %')

plt.title('PreTrain with AutoPET Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray',  'darkorange', 'darkorange'], yerr=yer, capsize=7)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/Cathi/Plots/10Per/ACC_AutoPET_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Cathi/Plots/10Per/ACC_AutoPET_image.png", format="png")
plt.savefig("/home/wolfda/Data/Cathi/Plots/10Per/ACC_AutoPET_pdf.pdf", format="pdf")

plt.show()

######################################################################################################################
# AUC AutoPET
# Höher der Bars (=Ergbnisse)
hight = [67.81
, 72.66
, 78.79

,79.23

]

# Namen der Bars
names = ['Scratch', 'All', 'Everyn', 'Hash']
x_pos = np.arange(len(names))

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [03.7779756

, 03.0334956

, 002.5262687


, 001.817557


]

# x-Achse
plt.ylim(60,85)

# X-Lable
plt.ylabel('AUC in %')

plt.title('PreTrain with AutoPET Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width,  color=['gray', 'gray', 'darkorange', 'darkorange'], yerr=yer, capsize=7,)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/Cathi/Plots/10Per/AUC_AutoPET_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Cathi/Plots/10Per/AUC_AutoPET_image.png", format="png")
plt.savefig("/home/wolfda/Data/Cathi/Plots/10Per/AUC_AutoPET_pdf.pdf", format="pdf")

plt.show()
#
# ######################################################################################################################
# F1 AutoPET
# Höher der Bars (=Ergbnisse)
hight = [44.716
, 53.54
, 67.36
, 72.528
]

# Namen der Bars
names = ['Scratch', 'All',  'Everyn', 'Hash']
x_pos = np.arange(len(names))

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [7.7393579

, 007.2989588

, 05.3956487


, 002.0046646

]

# x-Achse
plt.ylim(40,80)

# X-Lable
plt.ylabel('F1 in %')

plt.title('PreTrain with AutoPET Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray',  'darkorange', 'darkorange'], yerr=yer, capsize=7,)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/Cathi/Plots/10Per/F1_AutoPET_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Cathi/Plots/10Per/F1_AutoPET_image.png", format="png")
plt.savefig("/home/wolfda/Data/Cathi/Plots/10Per/F1_AutoPET_pdf.pdf", format="pdf")

plt.show()
#

#####################################################################################################################
# ACC LIDC
# Höher der Bars (=Ergbnisse)
hight = [59.64, 68.126, 69.28, 75.86, 75.88, 76.66
]

# Namen der Bars
names = ['Scratch', 'All',  'Everyn', 'Hash', 'SSIM', 'Mutal' ]
x_pos = np.arange(len(names))

#plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [3.4022786,  03.0334956, 01.2597619, 01.9918584, 02.7902697, 02.3567987


]

# x-Achse
plt.ylim(50,80)

# X-Lable
plt.ylabel('Accuracy in %')

plt.title('PreTrain with LIDC Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray', 'darkorange', 'darkorange', 'darkorange', 'darkorange'], yerr=yer, capsize=7)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/Cathi/Plots/10Per/Acc_LIDC_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Cathi/Plots/10Per/Acc_LIDC_image.png", format="png")
plt.savefig("/home/wolfda/Data/Cathi/Plots/10Per/Acc_LIDC_pdf.pdf", format="pdf")

plt.show()

######################################################################################################################
# AUC LIDC
# Höher der Bars (=Ergbnisse)
hight = [67.81, 73.428, 73.808, 81.904, 84.284, 80.028
]

# Namen der Bars
names = ['Scratch', 'All',  'Everyn', 'Hash', 'SSIM', 'Mutal' ]
x_pos = np.arange(len(names))

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [03.7779756,  03.0334956, 1.67, 3.37, 1.28, 2.10
]

# x-Achse
plt.ylim(60,90)

# X-Lable
plt.ylabel('AUC in %')

plt.title('PreTrain with LIDC Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width,  color=['gray', 'gray',   'darkorange', 'darkorange', 'darkorange', 'darkorange'], yerr=yer, capsize=7,)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/Cathi/Plots/10Per/AUC_LIDC_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Cathi/Plots/10Per/AUC_LIDC_image.png", format="png")
plt.savefig("/home/wolfda/Data/Cathi/Plots/10Per/AUC_LIDC_pdf.pdf", format="pdf")

plt.show()
#
# ######################################################################################################################
# F1 LIDC
# Höher der Bars (=Ergbnisse)
hight = [44.716
, 60.19

, 66.64



, 74.42



, 74.812




, 74.956



]

# Namen der Bars
names = ['Scratch', 'All',  'Everyn', 'Hash', 'SSIM', 'Mutal' ]
x_pos = np.arange(len(names))

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [ 7.7393579,  007.2989588, 1.91, 2.10, 2.74, 2.55

]

# x-Achse
plt.ylim(40,80)

# X-Lable
plt.ylabel('F1 in %')

plt.title('PreTrain with LIDC Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray',  'darkorange', 'darkorange', 'darkorange', 'darkorange'], yerr=yer, capsize=7,)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)


plt.savefig("/home/wolfda/Data/Cathi/Plots/10Per/F1_LIDC_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Cathi/Plots/10Per/F1_LIDC_image.png", format="png")
plt.savefig("/home/wolfda/Data/Cathi/Plots/10Per/F1_LIDC_pdf.pdf", format="pdf")


plt.show()