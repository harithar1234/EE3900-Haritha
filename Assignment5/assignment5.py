
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB


#generating circles

len = 100
p = np.zeros(2)

O_1 = np.array([1,0])
r_1=1
theta = np.linspace(0,2*np.pi,len)
x1_circ = np.zeros((2,len))
x1_circ[0,:] = r_1*np.cos(theta)
x1_circ[1,:] = r_1*np.sin(theta)
x1_circ = (x1_circ.T + O_1).T

O_2 = np.array([0,0])
r_2=1
theta = np.linspace(0,2*np.pi,len)
x2_circ = np.zeros((2,len))
x2_circ[0,:] = r_2*np.cos(theta)
x2_circ[1,:] = r_2*np.sin(theta)
x2_circ = (x2_circ.T + O_2).T

A= np.array([(0.5),((sqrt(3))*(0.5))])
B= np.array([(0.5),-((sqrt(3))*(0.5))]) 

#GENERATING LINES
x1_A=line_gen(O_1,A)
x1_B=line_gen(O_1,B)
x2_A=line_gen(O_2,A)
x2_B=line_gen(O_2,B)
x_AB = line_gen(A,B)


#Plotting all lines
plt.plot(x1_A[0,:],x1_A[1,:],label='$O_1 A$',color='orange')
plt.plot(x1_B[0,:],x1_B[1,:],label='$O_1 B$',color='red')
plt.plot(x2_A[0,:],x2_A[1,:],label='$O_2 A$',color='magenta')
plt.plot(x2_B[0,:],x2_B[1,:],label='$O_2 B$',color='cyan')
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$',color='brown')


#plotting circles
plt.plot(x1_circ[0,:],x1_circ[1,:],color='blue')
plt.plot(x2_circ[0,:],x2_circ[1,:],color='green')

#plotting points
plt.plot(A[0], A[1], 'o',color='black')
plt.text(A[0] * (1 + 0.1), A[1] * (1 + 0.1) , 'A')
plt.plot(B[0], B[1], 'o',color='black')
plt.text(B[0] * (1 - 0.1), B[1] * (1+0.2) , 'B')

#plotting centres
plt.plot(O_1[0], O_1[1], 'o',color='black')
plt.text(O_1[0] * (1 + 0.1), O_1[1] * (1 - 0.1) , 'O1')
plt.plot(O_2[0], O_2[1], 'o',color='black')
plt.text(O_2[0] -0.2 , O_2[1]-0.1  , 'O2')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid() # minor
plt.axis('equal')
plt.show()