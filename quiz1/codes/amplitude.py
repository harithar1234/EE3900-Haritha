
import matplotlib.pyplot as plt
import numpy as np
from math import *

n= np.arange(0,38, 0.1);
x  = np.sin((pi*n)/(19))

plt.plot(n,np.abs(x))
plt.grid()
plt.xlabel("n")
plt.ylabel("|x[n]|")

plt.show()