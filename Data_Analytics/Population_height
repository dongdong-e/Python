import numpy as np
data1 = np.loadtxt(fname = "NHIS_OPEN_GJ_20164.csv", delimiter = ",", encoding = "utf-8", dtype = np.str)

data2 = []

for i in data1[1:,3]:
    if i != '':
        data2.append(int(i))

h1 = []
h2 = []
h3 = []
h4 = []

for j in data2:
    if j < 160:
        h1.append(j)
    elif j < 170:
        h2.append(j)
    elif j < 180:
        h3.append(j)
    else:
        h4.append(j)

import matplotlib.pyplot as plt
plt.hist(len(h1))
plt.hist(len(h2))
plt.hist(len(h3))
plt.hist(len(h4))
plt.show()
