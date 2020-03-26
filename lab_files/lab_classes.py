# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 02:50:11 2020

@author: 1426391
Creating a Class¶
Now we are going to create a class circle, but first, we are going to import a library to draw the objects:
    The next step is a special method called a constructor __init__,
    which is used to initialize the object. The input are data attributes.
    The term self contains all the attributes in the set. For example the self.
    color gives the value of the attribute color and self.radius will give you the radius of the object. 
    We also have the method add_radius() with the parameter r, the method adds the value of r to
    the attribute radius. To access the radius we use the syntax self.radius.
"""
# Import the library

import matplotlib.pyplot as plt
%matplotlib inline

# Create a class Circle

class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show() 


# Create an object RedCircle
RedCircle = Circle(10, 'red')

# Find out the methods can be used on the object RedCircle
dir(RedCircle)

# Print the object attribute radius
RedCircle.radius

# Print the object attribute color
RedCircle.color

# Set the object attribute radius
RedCircle.radius = 1
RedCircle.radius

# Call the method drawCircle
RedCircle.drawCircle()

# Use method to change the object attribute radius
print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)

# Create a blue circle with a given radius
BlueCircle = Circle(radius=100)
# Print the object attribute color
BlueCircle.color
BlueCircle.drawCircle()



# Create a new Rectangle class for creating a rectangle object

class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()


# Create a new object rectangle
SkinnyBlueRectangle = Rectangle(2, 10, 'blue')
SkinnyBlueRectangle.height 
SkinnyBlueRectangle.width
SkinnyBlueRectangle.color
SkinnyBlueRectangle.drawRectangle()

# Create a new object rectangle
FatYellowRectangle = Rectangle(20, 5, 'yellow')

A=['1','2','3']

for a in A:
    print(2*a)





