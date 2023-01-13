import matplotlib.pyplot as plt
import numpy as np

######################################################################################################################
# ACC AutoPET
# Höher der Bars (=Ergbnisse)
hight = [67.288, 68.574, 73.892, 75.172, 76.41, 73.794, 75.662]

# Namen der Bars
names = ['Scratch', 'All', "Every-n", 'HashAll', 'Hash', 'SSIM', 'Mutal' ]
x_pos = np.arange(len(names))

#plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [02.6360792, 01.2205136, 0.634, 01.2265181, 01.3090964, 01.0797778, 00.7826323]

# x-Achse
plt.ylim(60,80)

# X-Lable
plt.ylabel('Accuracy in %')

plt.title('PreTrain with AutoPET Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray', "orange", 'darkorange', 'darkorange', 'darkorange', 'darkorange'], yerr=yer, capsize=7)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/ACC_AutoPET_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/ACC_AutoPET_image.png", format="png")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/ACC_AutoPET_pdf.pdf", format="pdf")

plt.show()

######################################################################################################################
# AUC AutoPET
# Höher der Bars (=Ergbnisse)
hight = [73.71
, 77.51, 80.161
, 81.702
, 82.992
, 81.992
, 83.836
]

# Namen der Bars
names = ['Scratch', 'All', "Every-n", 'HashAll', 'Hash', 'SSIM', 'Mutal' ]
x_pos = np.arange(len(names))

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [03.306917
, 00.8746999, 0.635
, 00.4581266
, 00.6935272
, 00.6079583
, 00.8859383
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

plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/AUC_AutoPET_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/AUC_AutoPET_image.png", format="png")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/AUC_AutoPET_pdf.pdf", format="pdf")

plt.show()
#
# ######################################################################################################################
# F1 AutoPET
# Höher der Bars (=Ergbnisse)
hight = [67.916
, 71.896, 75.106
, 77.142
, 77.716
, 76.084
, 77.236
]

# Namen der Bars
names = ['Scratch', 'All', "Every-n", 'HashAll', 'Hash', 'SSIM', 'Mutal' ]
x_pos = np.arange(len(names))

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [02.6783174
, 01.0416429, 1.011
, 00.9999733
, 01.4754954
, 0.8859383
, 0.6863818
]

# x-Achse
plt.ylim(60,80)

# X-Lable
plt.ylabel('F1 in %')

plt.title('PreTrain with AutoPET Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray', "orange", 'darkorange', 'darkorange', 'darkorange', 'darkorange'], yerr=yer, capsize=7,)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/F1_AutoPET_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/F1_AutoPET_image.png", format="png")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/F1_AutoPET_pdf.pdf", format="pdf")

plt.show()
#

#####################################################################################################################
# ACC LIDC
# Höher der Bars (=Ergbnisse)
hight = [67.288, 71.23
, 73.958
, 75.962
, 75.466
, 73.4
, 72.906
]

# Namen der Bars
names = ['Scratch', 'All', "Every-n", 'HashAll', 'Hash', 'SSIM', 'Mutal' ]
x_pos = np.arange(len(names))

#plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [02.6360792, 1.5739123, 1.115
, 00.7198009
, 00.7182061
, 01.0256218
, 00.8982687
]

# x-Achse
plt.ylim(60,80)

# X-Lable
plt.ylabel('Accuracy in %')

plt.title('PreTrain with LIDC Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray', "orange", 'darkorange', 'darkorange', 'darkorange', 'darkorange'], yerr=yer, capsize=7)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/Acc_LIDC_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/Acc_LIDC_image.png", format="png")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/Acc_LIDC_pdf.pdf", format="pdf")

plt.show()

######################################################################################################################
# AUC LIDC
# Höher der Bars (=Ergbnisse)
hight = [73.71
, 80.73
, 81.502
, 82.572

, 82.314

, 80.562

, 81.55

]

# Namen der Bars
names = ['Scratch', 'All', "Every-n", 'HashAll', 'Hash', 'SSIM', 'Mutal' ]
x_pos = np.arange(len(names))

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [03.306917

,0.5893782
, 0.86
, 0.688341

, 0.4132231

, 0.7416738

, 0.3806573

]

# x-Achse
plt.ylim(60,90)

# X-Lable
plt.ylabel('AUC in %')

plt.title('PreTrain with LIDC Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width,  color=['gray', 'gray', "orange",  'darkorange', 'darkorange', 'darkorange', 'darkorange'], yerr=yer, capsize=7,)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/AUC_LIDC_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/AUC_LIDC_image.png", format="png")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/AUC_LIDC_pdf.pdf", format="pdf")

plt.show()
#
# ######################################################################################################################
# F1 LIDC
# Höher der Bars (=Ergbnisse)
hight = [67.916
, 74.388
, 75.186
, 77.248


, 76.788


, 74.76



, 74.27


]

# Namen der Bars
names = ['Scratch', 'All', "Every-n", 'HashAll', 'Hash', 'SSIM', 'Mutal' ]
x_pos = np.arange(len(names))

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [02.6783174
, 01.3095979
, 1.2
,0.5507994

,00.7452606

, 00.8555895

,00.8790715

]

# x-Achse
plt.ylim(60,80)

# X-Lable
plt.ylabel('F1 in %')

plt.title('PreTrain with LIDC Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray', "orange", 'darkorange', 'darkorange', 'darkorange', 'darkorange'], yerr=yer, capsize=7,)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)


plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/F1_LIDC_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/F1_LIDC_image.png", format="png")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/F1_LIDC_pdf.pdf", format="pdf")


plt.show()