
import numpy as np
import matplotlib.pyplot as plt

def line_dir_pt(m,A,k1,k2):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

#Inputs
A_1 = np.array([-2,-1]) 
A = np.array([-2,3]) #point
m = np.array([4,3])  #slope
k1=-1
k2=1
#Generating lines
x_r = line_dir_pt(m,A,k1,k2)
x_g = line_dir_pt(m,A_1,k1,k2)

#Plotting all lines
plt.plot(x_r[0,:],x_r[1,:],label='required line')
plt.plot(x_g[0,:],x_g[1,:],label='given line')

#plotting point
plt.plot(A[0], A[1], 'o')
plt.text(A[0] , A[1] , '(-2,3)')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor

plt.show()