import matplotlib.pyplot as plt
import numpy as np
#
# ######################################################################################################################
# # AutoPET PreTrain
# # Höher der Bars (=Ergbnisse)
# hight = [0
# , 538
# , 24
# ]
#
# # Namen der Bars
# names = ['Scratch', 'All', "10-Perc"]
# x_pos = np.arange(len(names))
#
# #plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]
#
# # Breite der Bars
# width = [0.5, 0.5, 0.5]
#
#
# # x-Achse
# plt.ylim(0,600)
#
# # X-Lable
# plt.ylabel('Time in Hour')
#
# plt.title('AutoPET')
#
# # Plot: bars, bars label, x labels
# rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray','darkorange'], capsize=7)
# plt.bar_label(rects, padding=3)
# plt.xticks(x_pos, names)
#
# plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/PreTrain_AutoPET_vec.eps", format="eps")
# plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/PreTrain_AutoPET_image.png", format="png")
# plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/PreTrain_AutoPET_pdf.pdf", format="pdf")
#
# plt.show()
#
# ######################################################################################################################
# # LIDC PreTrain
# # Höher der Bars (=Ergbnisse)
# hight = [0, 280,
# 53
# ]
#
# # Namen der Bars
# names = ['Scratch', 'All',  "10-Perc"]
# x_pos = np.arange(len(names))
#
# #plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]
#
# # Breite der Bars
# width = [0.5, 0.5, 0.5]
#
#
# # x-Achse
# plt.ylim(0,600)
#
# # X-Lable
# plt.ylabel('Time in Hour')
#
# plt.title('LIDC')
#
# # Plot: bars, bars label, x labels
# rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray', 'darkorange'], capsize=7)
# plt.bar_label(rects, padding=3)
# plt.xticks(x_pos, names)
#
# plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/PreTrain_LIDC_vec.eps", format="eps")
# plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/PreTrain_LIDC_image.png", format="png")
# plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/PreTrain_LIDC_pdf.pdf", format="pdf")
#
# plt.show()
#
# ######################################################################################################################
# # Similarity AutoPET
# # Höher der Bars (=Ergbnisse)
# hight = [0
# , 3
# , 340
# , 312
# ]
#
# # Namen der Bars
# names = ['All','Hash', 'SSIM', "Muatl"]
# x_pos = np.arange(len(names))
#
# #plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]
#
# # Breite der Bars
# width = [0.5, 0.5, 0.5, 0.5]
#
#
# # x-Achse
# plt.ylim(0,600)
#
# # X-Lable
# plt.ylabel('Time in Hour')
#
# plt.title('AutoPET')
#
# # Plot: bars, bars label, x labels
# rects = plt.bar(x_pos, hight, width= width, color=['gray', 'darkorange', 'darkorange', 'darkorange'], capsize=7)
# plt.bar_label(rects, padding=3)
# plt.xticks(x_pos, names)
#
# plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/Similarity_AutoPET_vec.eps", format="eps")
# plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/Similarity_AutoPET_image.png", format="png")
# plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/Similarity_AutoPET_pdf.pdf", format="pdf")
#
# plt.show()
#
#
# ######################################################################################################################
# # Similarity LIDC
# # Höher der Bars (=Ergbnisse)
# hight = [0
# , 2
# , 92
# , 90
# ]
#
# # Namen der Bars
# names = ['All', 'Hash', 'SSIM', "Muatl"]
# x_pos = np.arange(len(names))
#
# #plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]
#
# # Breite der Bars
# width = [0.5, 0.5, 0.5, 0.5]
#
#
# # x-Achse
# plt.ylim(0,600)
#
# # X-Lable
# plt.ylabel('Time in Hour')
#
# plt.title('LIDC')
#
# # Plot: bars, bars label, x labels
# rects = plt.bar(x_pos, hight, width= width, color=['gray', 'darkorange', 'darkorange', 'darkorange'], capsize=7)
# plt.bar_label(rects, padding=3)
# plt.xticks(x_pos, names)
#
# plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/Similarity_LIDC_vec.eps", format="eps")
# plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/Similarity_LIDC_image.png", format="png")
# plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/Similarity_LIDC_pdf.pdf", format="pdf")
#
# plt.show()
#
# #########################################################################################################
# # Together
# #########################################################################################################
# # AutoPET
#
# # Höher der Bars (=Ergbnisse)
# simi = [0, 0
# , 3
# , 340
# , 312
# ]
#
# pretrain = [
# 538,
# 53,
# 53, 53, 53
# ]
#
# # Namen der Bars
# names = ['All',"Everyn", 'Hash', 'SSIM', "Mutual"]
# x_pos = np.arange(len(names))
#
# #plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]
#
# # Breite der Bars
# width = [0.5, 0.5, 0.5, 0.5, 0.5]
#
#
# # x-Achse
# plt.ylim(0,600)
#
# # X-Lable
# plt.ylabel('Time in Hour')
#
# plt.title('AutoPET')
#
# # Plot: bars, bars label, x labels
# rects = plt.bar(x_pos, simi, width= width, color=['blue', 'blue', 'blue', 'blue', "blue"], capsize=7, label='Similarity')
# rects = plt.bar(x_pos, pretrain, width= width, color=['red', 'red', 'red', 'red', "red"], capsize=7, bottom=simi, label="Pre-training")
# plt.bar_label(rects, padding=3)
# plt.xticks(x_pos, names)
# plt.legend()
#
# plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/All_AutoPET_vec.eps", format="eps")
# plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/All_AutoPET_image.png", format="png")
# plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/All_AutoPET_pdf.pdf", format="pdf")
#
# plt.show()
#
#
# ######################################################################################################################
# # Similarity LIDC
# # Höher der Bars (=Ergbnisse)
# simi = [0, 0
# , 2
# , 92
# , 90
# ]
#
# pretrain = [280, 24, 24, 24, 24
# ]
#
# # Namen der Bars
# names = ['All', "Everyn", 'Hash', 'SSIM', "Muatl"]
# x_pos = np.arange(len(names))
#
# #plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]
#
# # Breite der Bars
# width = [0.5, 0.5, 0.5, 0.5, 0.5]
#
#
# # x-Achse
# plt.ylim(0,600)
#
# # X-Lable
# plt.ylabel('Time in Hour')
#
# plt.title('LIDC')
#
# # Plot: bars, bars label, x labels
# rects = plt.bar(x_pos, simi, width= width, color=['blue', 'blue', 'blue', 'blue', 'blue'], capsize=7, label='Similarity')
# rects = plt.bar(x_pos, pretrain, width= width, color=['red', 'red', 'red', 'red', "red"], capsize=7, bottom=simi, label="Pre-training")
# plt.bar_label(rects, padding=3)
# plt.xticks(x_pos, names)
# plt.legend()
#
# plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/All_LIDC_vec.eps", format="eps")
# plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/All_LIDC_image.png", format="png")
# plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/All_LIDC_pdf.pdf", format="pdf")
#
# plt.show()

#################################################################################################################
# Hash 6
#################################################################################################################
# AutoPET

# Höher der Bars (=Ergbnisse)
simi = [0, 0
]

pretrain = [
538,
62,

]

# Namen der Bars
names = ['All',"Hash-6"]
x_pos = np.arange(len(names))

#plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]

# Breite der Bars
width = [0.5, 0.5]


# x-Achse
plt.ylim(0,600)

# X-Lable
plt.ylabel('Time in Hour')

plt.title('AutoPET')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, simi, width= width, color=['blue', 'blue'], capsize=7, label='Similarity')
rects = plt.bar(x_pos, pretrain, width= width, color=['red', 'red'], capsize=7, bottom=simi, label="Pre-training")
plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)
plt.legend()

plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/Hash6_AutoPET_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/Hash6_AutoPET_image.png", format="png")
plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/Hash6_AutoPET_pdf.pdf", format="pdf")

plt.show()


######################################################################################################################
# Similarity LIDC
# Höher der Bars (=Ergbnisse)
simi = [0, 0
]

pretrain = [280,  27
]

# Namen der Bars
names = ['All',  'Hash-6']
x_pos = np.arange(len(names))

#plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]

# Breite der Bars
width = [0.5, 0.5]


# x-Achse
plt.ylim(0,600)

# X-Lable
plt.ylabel('Time in Hour')

plt.title('LIDC')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, simi, width= width, color=['blue', 'blue'], capsize=7, label='Similarity')
rects = plt.bar(x_pos, pretrain, width= width, color=['red', 'red'], capsize=7, bottom=simi, label="Pre-training")
plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)
plt.legend()

plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/Hash6_LIDC_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/Hash6_LIDC_image.png", format="png")
plt.savefig("/home/wolfda/Data/PreTrain_LIDC_AutoPET/Plots/New/Hash6_LIDC_pdf.pdf", format="pdf")

plt.show()