# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 00:14:44 2020

@author: ahmed
"""


# Import the libraries
import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt
#%matplotlib inline  

# Plotting functions
def Plotvec1(u, z, v):
    
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

def Plotvec2(a,b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)
    
    

"""What is Numpy?
A numpy array is similar to a list. 
It's usually fixed in size and each element is of the same type.
 We can cast a list to a numpy array by first importing numpy:"""

# import numpy library
import numpy as np 
# Create a list
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
a
# We then cast the list as follows:
# Convert list to Numpy Array
# Every element is the same type
A = np.array(a)
A

A.ndim
"""Attribute <code>shape</code> returns a tuple corresponding to the size or number of each dimension."""
A.shape

A.size

# Access the element on the second row and third column
A[1, 2]
# Or
A[1][2]

# Access the element on the first row and first and second columns
A[0][0:2]

# Access the element on the first and second rows and third column
A[1:3, 2]

# Create a numpy array X
X = np.array([[1, 0], [0, 1]]) 
X

# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
Y

# Add X and Y
Z = X + Y
Z

# Multiply Y with 2
Z = 2 * Y

# Multiply X with Y
Z = X * Y
Z

# Create a matrix A
A = np.array([[0, 1, 1], [1, 0, 1]])
A
# Create a matrix B
B = np.array([[1, 1], [1, 1], [-1, 1]])
B

# Calculate the dot product
Z = np.dot(A,B)
Z

# Calculate the sine of Z
np.sin(Z)
"""We use the numpy attribute <code>T</code> to calculate the transposed matrix"""
# Create a matrix C
C = np.array([[1,1],[2,2],[3,3]])
C
# Get the transposed of C
C.T

a=np.array([0,1,0,1,0])

b=np.array([1,0,1,0,1])

a*b








# Create a numpy array
A=np.array([[1,2],[3,4],[5,6],[7,8]])
B=np.array([[1,2,3],[4,5,6],[7,8,9]])
np.dot(A,B)

A=np.array([[1,2],[3,4],[5,6],[7,8]])
A



