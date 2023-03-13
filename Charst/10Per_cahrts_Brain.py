import matplotlib.pyplot as plt
import numpy as np


# Höher der Bars (=Ergbnisse)
hight = [59.64,
62.76
, 73.79
, 73.79
]

# Namen der Bars
names = ['Scratch', 'All', 'Everyn', 'Hash' ]
x_pos = np.arange(len(names))


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

