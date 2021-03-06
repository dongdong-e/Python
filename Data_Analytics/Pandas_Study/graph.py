import pandas as pd
import numpy as np
import seaborn as sns
%matplotlib notebook
import matplotlib.pyplot as plt

plt.figure(figsize = (10, 5))
t = np.arange(0, 5, 0.5)
plt.plot(t, t, "r--")
plt.plot(t, t ** 3, "gx")
plt.plot(t, t ** 2.5, color = "green", linestyle = "dashed", marker = "o")

# plot
s1 = np.random.normal(loc = 0, scale = 1, size = 1000)
s2 = np.random.normal(loc = 5, scale = 0.5, size = 1000)
s3 = np.random.normal(loc = 10, scale = 2, size = 1000)
plt.plot(s1, label = "s1")
plt.plot(s2, label = "s2")
plt.plot(s3, label = "s3")
plt.legend()
plt.show()

# boxplot
plt.figure(figsize = (10, 6))
plt.boxplot((s1, s2, s3))
plt.show()
