import matplotlib.pyplot as plt
import numpy as np

######################################################################################################################
# ACC AutoPET
# Höher der Bars (=Ergbnisse)
hight = [67.288,
68.574
, 74.284
, 74.286
]

# Namen der Bars
names = ['Scratch', 'All', 'Everyn', 'Hash' ]
x_pos = np.arange(len(names))

#plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [02.6360792
, 01.2205136
, 01.4598699
,00.7731882
]

# x-Achse
plt.ylim(60,80)

# X-Lable
plt.ylabel('Accuracy in %')

plt.title('PreTrain with AutoPET Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray',  'darkorange', 'darkorange'], yerr=yer, capsize=7)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/10Per/ACC_AutoPET_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/10Per/ACC_AutoPET_image.png", format="png")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/10Per/ACC_AutoPET_pdf.pdf", format="pdf")

plt.show()

######################################################################################################################
# AUC AutoPET
# Höher der Bars (=Ergbnisse)
hight = [73.71
, 77.51
, 81.022

, 82.51

]

# Namen der Bars
names = ['Scratch', 'All', 'Everyn', 'Hash']
x_pos = np.arange(len(names))

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [03.306917
, 00.8746999
, 0.7115101

, 0.3716181

]

# x-Achse
plt.ylim(70,85)

# X-Lable
plt.ylabel('AUC in %')

plt.title('PreTrain with AutoPET Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width,  color=['gray', 'gray', 'darkorange', 'darkorange'], yerr=yer, capsize=7,)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/10Per/AUC_AutoPET_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/10Per/AUC_AutoPET_image.png", format="png")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/10Per/AUC_AutoPET_pdf.pdf", format="pdf")

plt.show()
#
# ######################################################################################################################
# F1 AutoPET
# Höher der Bars (=Ergbnisse)
hight = [67.916
, 71.896
, 75.872
, 75.568
]

# Namen der Bars
names = ['Scratch', 'All',  'Everyn', 'Hash']
x_pos = np.arange(len(names))

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [02.6783174
, 01.0416429
, 01.6048821

, 01.0214924
]

# x-Achse
plt.ylim(60,80)

# X-Lable
plt.ylabel('F1 in %')

plt.title('PreTrain with AutoPET Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray',  'darkorange', 'darkorange'], yerr=yer, capsize=7,)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/10Per/F1_AutoPET_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/10Per/F1_AutoPET_image.png", format="png")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/10Per/F1_AutoPET_pdf.pdf", format="pdf")

plt.show()
#

#####################################################################################################################
# ACC LIDC
# Höher der Bars (=Ergbnisse)
hight = [67.288, 71.23
, 73.794
, 73.692

, 74.582

, 74.87

]

# Namen der Bars
names = ['Scratch', 'All',  'Everyn', 'Hash', 'SSIM', 'Mutal' ]
x_pos = np.arange(len(names))

#plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [02.6360792, 1.5739123
, 0.9996433

, 0.9699725



, 0.6105298

, 02.8085465

]

# x-Achse
plt.ylim(60,80)

# X-Lable
plt.ylabel('Accuracy in %')

plt.title('PreTrain with LIDC Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray', 'darkorange', 'darkorange', 'darkorange', 'darkorange'], yerr=yer, capsize=7)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/10Per/Acc_LIDC_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/10Per/Acc_LIDC_image.png", format="png")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/10Per/Acc_LIDC_pdf.pdf", format="pdf")

plt.show()

######################################################################################################################
# AUC LIDC
# Höher der Bars (=Ergbnisse)
hight = [73.71
, 80.73

, 81.064


, 82.554


, 82.468


, 81.974


]

# Namen der Bars
names = ['Scratch', 'All',  'Everyn', 'Hash', 'SSIM', 'Mutal' ]
x_pos = np.arange(len(names))

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [03.306917

,0.5893782
, 0.5832267



, 01.0207612



, 0.3142398



, 0.6653721


]

# x-Achse
plt.ylim(65,85)

# X-Lable
plt.ylabel('AUC in %')

plt.title('PreTrain with LIDC Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width,  color=['gray', 'gray',   'darkorange', 'darkorange', 'darkorange', 'darkorange'], yerr=yer, capsize=7,)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/10Per/AUC_LIDC_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/10Per/AUC_LIDC_image.png", format="png")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/10Per/AUC_LIDC_pdf.pdf", format="pdf")

plt.show()
#
# ######################################################################################################################
# F1 LIDC
# Höher der Bars (=Ergbnisse)
hight = [67.916
, 74.388

, 75.582



, 75.408



, 75.652




, 75.438



]

# Namen der Bars
names = ['Scratch', 'All',  'Everyn', 'Hash', 'SSIM', 'Mutal' ]
x_pos = np.arange(len(names))

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [02.6783174
, 01.3095979

,01.0331892


,01.3291777


, 0.8133757


,01.0772248


]

# x-Achse
plt.ylim(65,80)

# X-Lable
plt.ylabel('F1 in %')

plt.title('PreTrain with LIDC Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray',  'darkorange', 'darkorange', 'darkorange', 'darkorange'], yerr=yer, capsize=7,)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)


plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/10Per/F1_LIDC_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/10Per/F1_LIDC_image.png", format="png")
plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/10Per/F1_LIDC_pdf.pdf", format="pdf")


plt.show()