import matplotlib.pyplot as plt
import numpy as np

# ######################################################################################################################
# # ACC AutoPET
# # Höher der Bars (=Ergbnisse)
# hight = [67.288,
# 68.574
# , 74.284
# , 74.286
# ]
#
# # Namen der Bars
# names = ['Scratch', 'All', 'Hash-3', 'Hash-6', "Hash-12" ]
# x_pos = np.arange(len(names))
#
# #plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]
#
# # Breite der Bars
# width = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
#
# # Error bars
# yer = [02.6360792
# , 01.2205136
# , 01.4598699
# ,00.7731882
# ]
#
# # x-Achse
# plt.ylim(60,80)
#
# # X-Lable
# plt.ylabel('Accuracy in %')
#
# plt.title('PreTrain with AutoPET Dataset')
#
# # Plot: bars, bars label, x labels
# rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray',  'darkorange', 'darkorange'], yerr=yer, capsize=7)
# #plt.bar_label(rects, padding=3)
# plt.xticks(x_pos, names)
#
# plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/Border/ACC_AutoPET_vec.eps", format="eps")
# plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/Border/ACC_AutoPET_image.png", format="png")
# plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/Border/ACC_AutoPET_pdf.pdf", format="pdf")
#
# plt.show()

######################################################################################################################
# AUC AutoPET
# Höher der Bars (=Ergbnisse)
hight = [67.81


, 72.666

, 79.904




, 83.18


, 76.764


]

# Namen der Bars
names = ['Scratch', 'All', 'Hash-3', 'Hash-6', "Hash-12" ]
x_pos = np.arange(len(names))

#plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [03.7779756

, 03.0334956
, 01.21079312849058



, 02.75784615135883


, 03.09032145037804


]

# x-Achse
plt.ylim(60,90)

# X-Lable
plt.ylabel('AUC in %')

plt.title('PreTrain with AutoPET Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width,  color=['gray', 'gray', 'darkorange', 'darkorange', 'darkorange'], yerr=yer, capsize=7,)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/Cathi/Plots/Border/AUC_AutoPET_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Cathi/Plots/Border/AUC_AutoPET_image.png", format="png")
plt.savefig("/home/wolfda/Data/Cathi/Plots/Border/AUC_AutoPET_pdf.pdf", format="pdf")

plt.show()
#
# ######################################################################################################################
# F1 AutoPET
# Höher der Bars (=Ergbnisse)
hight = [044.716


, 053.45


, 068.714





, 076.494



, 069.66



]

names = ['Scratch', 'All', 'Hash-3', 'Hash-6', "Hash-12" ]
x_pos = np.arange(len(names))

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [7.7393579

, 007.2989588
, 001.66990618498965





, 02.42835746956662

, 03.52921143222298



]

# x-Achse
plt.ylim(40,80)

# X-Lable
plt.ylabel('F1 in %')

plt.title('PreTrain with AutoPET Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray',  'darkorange', 'darkorange', 'darkorange'], yerr=yer, capsize=7,)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/Cathi/Plots/Border/F1_AutoPET_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Cathi/Plots/Border/F1_AutoPET_image.png", format="png")
plt.savefig("/home/wolfda/Data/Cathi/Plots/Border/F1_AutoPET_pdf.pdf", format="pdf")

plt.show()


#####################################################################################################################
# # ACC LIDC
# # Höher der Bars (=Ergbnisse)
# hight = [67.288, 71.23
# , 73.794
# , 73.692
#
# , 74.582
#
# , 74.87
#
# ]
#
# # Namen der Bars
# names = ['Scratch', 'All',  'Everyn', 'Hash', 'SSIM', 'Mutal' ]
# x_pos = np.arange(len(names))
#
# #plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]
#
# # Breite der Bars
# width = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
#
# # Error bars
# yer = [02.6360792, 1.5739123
# , 0.9996433
#
# , 0.9699725
#
#
#
# , 0.6105298
#
# , 02.8085465
#
# ]
#
# # x-Achse
# plt.ylim(60,80)
#
# # X-Lable
# plt.ylabel('Accuracy in %')
#
# plt.title('PreTrain with LIDC Dataset')
#
# # Plot: bars, bars label, x labels
# rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray', 'darkorange', 'darkorange', 'darkorange', 'darkorange'], yerr=yer, capsize=7)
# #plt.bar_label(rects, padding=3)
# plt.xticks(x_pos, names)
#
# plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/10Per/Acc_LIDC_vec.eps", format="eps")
# plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/10Per/Acc_LIDC_image.png", format="png")
# plt.savefig("/home/wolfda/Data/Covid-Classification/Plots/10Per/Acc_LIDC_pdf.pdf", format="pdf")
#
# plt.show()

######################################################################################################################
# AUC LIDC
# Höher der Bars (=Ergbnisse)
hight = [67.81, 73.428

, 079.048




, 084.064




, 079.81




]

# Namen der Bars
names = ['Scratch', 'All',  'Hash-3', 'Hash-6', 'Hash-12' ]
x_pos = np.arange(len(names))

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [03.7779756,  03.0334956
, 0.869969348119039





, 01.68530511579753





, 002.61519279085373







]

# x-Achse
plt.ylim(60,90)

# X-Lable
plt.ylabel('AUC in %')

plt.title('PreTrain with LIDC Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width,  color=['gray', 'gray',   'darkorange', 'darkorange', 'darkorange'], yerr=yer, capsize=7,)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/Cathi/Plots/Border/AUC_LIDC_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Cathi/Plots/Border/AUC_LIDC_image.png", format="png")
plt.savefig("/home/wolfda/Data/Cathi/Plots/Border/AUC_LIDC_pdf.pdf", format="pdf")

plt.show()
#
# ######################################################################################################################
# F1 LIDC
# Höher der Bars (=Ergbnisse)
hight = [44.716
, 60.19

, 072.348





, 080.02





, 067.772




]

# Namen der Bars
names = ['Scratch', 'All',  'Hash-3', 'Hash-6', 'Hash-12']
x_pos = np.arange(len(names))

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5, 0.5]

# Error bars
yer = [7.7393579,  007.2989588

,003.73918618596792





,02.97153720039533





, 002.39982221563737




]

# x-Achse
plt.ylim(40,90)

# X-Lable
plt.ylabel('F1 in %')

plt.title('PreTrain with LIDC Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray',  'darkorange', 'darkorange', 'darkorange'], yerr=yer, capsize=7,)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)


plt.savefig("/home/wolfda/Data/Cathi/Plots/Border/F1_LIDC_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Cathi/Plots/Border/F1_LIDC_image.png", format="png")
plt.savefig("/home/wolfda/Data/Cathi/Plots/Border/F1_LIDC_pdf.pdf", format="pdf")


plt.show()