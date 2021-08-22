# -*- coding: utf-8 -*-
"""assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zanI8hmtcyy9zZYGqaYp3eLufid4txL1
"""

# Code to verify the matrix as symmetric or skew symmetric ##
#importing numpy and matplotlib libraries
import numpy as np
import matplotlib.pyplot as plt

## Given matrix 
A= np.array([[1,5],[6,7]])
print("A:\n",A)
# Finding transpose
A_trans = A.T
print("Transpose of A:\n",A_trans)

#(i)
SUM=A+A_trans
SUM_trans=SUM.T
print("\n(A+Transpose of A):\n",SUM)
# Finding whether the matrix is symmetric
delta= SUM-SUM_trans
#delta is null matrix
if (delta.all()==0):
  print("(A+Transpose of A) is a symmetric matrix")
  
#(ii)
DIFF=A-A_trans
DIFF_trans=DIFF.T
print("\n(A-Transpose of A):\n",DIFF)
# Finding whether the matrix is skew symmetric
delta= DIFF+DIFF_trans
#delta is null matrix
if (delta.all()==0):
  print("(A-Transpose of A) is a skew symmetric matrix")