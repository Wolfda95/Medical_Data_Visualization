import matplotlib.pyplot as plt
import numpy as np

######################################################################################################################
# ACC PadChest
# Höher der Bars (=Ergbnisse)
hight = [74.36
, 84.62
, 82.21
, 80.13
]

# Namen der Bars
names = ['Scratch', 'All', 'Hash', 'ImageNet']
x_pos = np.arange(len(names))

#plt.figure(figsize = [5.4, 4.8]) # Default:  [6.4, 4.8]

# Breite der Bars
width = [0.5, 0.5, 0.5, 0.5]


# x-Achse
plt.ylim(60,90)

# X-Lable
plt.ylabel('Accuracy in %')

plt.title('PreTrain with PadChest Dataset')

# Plot: bars, bars label, x labels
rects = plt.bar(x_pos, hight, width= width, color=['gray', 'gray', 'darkorange', 'red'], capsize=7)
#plt.bar_label(rects, padding=3)
plt.xticks(x_pos, names)

plt.savefig("/home/wolfda/Data/Chest_X-Ray/Plots/ACC_PedChest_vec.eps", format="eps")
plt.savefig("/home/wolfda/Data/Chest_X-Ray/Plots/ACC_PedChest_image.png", format="png")
plt.savefig("/home/wolfda/Data/Chest_X-Ray/Plots/ACC_PedChest_pdf.pdf", format="pdf")

plt.show()

