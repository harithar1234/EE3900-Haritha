
import numpy as np
import matplotlib.pyplot as plt

a = 10
c = 6
b = np.sqrt((a*a)-(c*c))

e = ((a*a) + (c*c)-(b*b))/(2*a)
f = np.sqrt((c*c)-(e*e))

#points
A = np.array([e,f]) 
B = np.array([0,0]) 
C = np.array([a,0]) 
D = np.array([e,-f]) 

#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_CD = line_gen(C,D)

#Plotting tangents- CD,CA; radius-AB ;line-BC
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 - 0.2), D[1] * (1) , 'D')

#Plot circle
theta = np.linspace(0,2*np.pi,50)
x = c*np.cos(theta)
y = c*np.sin(theta)
plt.plot(x,y)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()