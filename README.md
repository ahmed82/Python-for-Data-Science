# Python-for-Data-Science

## Module 1 - Python Basics

Your first program
Types
Expressions and Variables
String Operations

## Module 2 - Python Data Structures

Lists and Tuples
Sets
Dictionaries

## Module 3 - Python Programming Fundamentals

Conditions and Branching
Loops
Functions
Objects and Classes

## Module 4 - Working with Data in Python

Reading files with open
Writing files with open
Loading data with Pandas
Working with and Saving data with Pandas

## Module 5 - Working with Numpy Arrays
Numpy 1D Arrays
Numpy 2D Arrays
---
## References
Lutz, Mark. Learning Python: Powerful Object-Oriented Programming. " O'Reilly Media, Inc.", 2013.
Ana Bell, Eric Grimson and John Guttag.  Introduction to Computer Science and Programming in Python, MIT Open Course Ware, MIT 2017
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
---
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