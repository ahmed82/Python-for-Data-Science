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
    
    
# Create a python list
a = ["0", 1, "two", "3", 4]

#We can access each element using a square bracket as follows: 
# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])


"""What is Numpy?
A numpy array is similar to a list. 
It's usually fixed in size and each element is of the same type.
 We can cast a list to a numpy array by first importing numpy:"""

# import numpy library
import numpy as np 
# We then cast the list as follows:
# Create a numpy array

a = np.array([0, 1, 2, 3, 4])
a
# Test line 47 - 51

"""If we check the type of the array we get <b>numpy.ndarray</b>:"""
# Check the type of the array
type(a)

# Check the type of the values stored in numpy array
a.dtype

"""We can create a numpy array with real numbers:"""
# Create a numpy array
b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
b.dtype

"""We can change the value of the array"""
c = np.array([20, 1, 2, 3, 4])
c
# Assign the first element to 100
c[0] = 100
c

"""
Like lists, we can slice the numpy array, and we can select the elements from 1 to 3 
and assign it to a new numpy array <code>d</code> as follows:
"""
# Slicing the numpy array
d = c[1:4]
d
# Set the fourth element and fifth element to 300 and 400
c[3:5] = 300, 400
c

"""Assign Value with List"""
# Create the index list
select = [0, 2, 3]
# Use List to select elements
d = c[select]
d

# Assign the specified elements to new value
c[select] = 100000
c

# Create a numpy array
a = np.array([0, 1, 2, 3, 4])
a

# Get the size of numpy array
a.size
# Get the number of dimensions of numpy array
a.ndim

"""The attribute <code>shape</code> is a tuple of integers indicating the size of the array in each dimension:"""
# Get the shape/size of numpy array
a.shape

# Create a numpy array
a = np.array([1, -1, 1, -1])
# Get the mean of numpy array
mean = a.mean()
mean
# Get the standard deviation of numpy array
standard_deviation=a.std()
standard_deviation

# Create a numpy array
b = np.array([-1, 2, 3, 4, 5])
# Get the biggest value in the numpy array
max_b = b.max()
max_b
# Get the smallest value in the numpy array
min_b = b.min()
min_b


"""
Numpy Array Operations
"""
u = np.array([1, 0])
u
v = np.array([0, 1])
v
# Numpy Array Addition
z = u + v
z
# Plot numpy arrays
Plotvec1(u, z, v)

y = np.array([1, 2])
y
# Numpy Array Multiplication
z = 2 * y
z

u = np.array([1, 2])
u
v = np.array([3, 2])
v
# Calculate the production of two numpy arrays
z = u * v
z

# Calculate the dot product
np.dot(u, v)

# Create a constant to numpy array
u = np.array([1, 2, 3, -1]) 
u

# Add the constant to array
u + 1

# The value of pie
np.pi

# Create the numpy array in radians
x = np.array([0, np.pi/2 , np.pi])

"""
We can apply the function sin to the array x and assign the values 
to the array y; this applies the sine function to each element in the array:
"""
# Calculate the sin of each elements
y = np.sin(x)
y

"""
Linspace
A useful function for plotting mathematical functions is "linespace".
 Linespace returns evenly spaced numbers over a specified interval. 
 We specify the starting point of the sequence and the ending point of the sequence.
 The parameter "num" indicates the Number of samples to generate, in this case 5:
"""
# Makeup a numpy array within [-2, 2] and 5 elements
np.linspace(-2, 2, num=5)
#If we change the parameter <code>num</code> to 9,
# we get 9 evenly spaced numbers over the interval from -2 to 2: 

"""
We can use the function line space to generate 100 evenly spaced samples from the interval 0 to 2π: 
"""
# Makeup a numpy array within [0, 2π] and 100 elements 
x = np.linspace(0, 2*np.pi, num=100)
# Calculate the sine of x list
y = np.sin(x)
# Plot the result
plt.plot(x, y)


#Convert the list [-1, 1] and [1, 1] to numpy arrays a and b. Then, 
#plot the arrays as vectors using the fuction Plotvec2 and find the dot product:
a = np.array([-1, 1])
b = np.array([1, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a,b))



"""
Why are the results of the dot product for [-1, 1] and [1, 1] and the dot product for [1, 0] and [0, 1] zero, but not zero for the dot product for [1, 1] and [0, 1]?

Hint: Study the corresponding figures, pay attention to the direction the arrows are pointing to.
<!-- 
The vectors used for question 4 and 5 are perpendicular. As a result, the dot product is zero. 
-->
https://cognitiveclass.ai/blog/data-scientists-stand-out-by-sharing-your-notebooks
"""





