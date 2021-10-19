

import matplotlib.pyplot as plt
import numpy as np
from math import *

n= np.arange(0,76, 0.1);
x  = np.sin((pi*n)/(19))

plt.plot(n,np.angle(x))
plt.grid()
plt.xlabel("n")
plt.ylabel("arg(x[n])")

plt.show()