# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 03:14:56 2020

@author: 1426391
Reading Text Files
One way to read or write a file in Python is to use the built-in open function.
 The open function provides a File object that contains the methods and attributes
 you need in order to read, save, and manipulate the file.
 In this notebook, we will only cover .txt files. 
 The first parameter you need is the file path and the file name. An example is shown as follow:
"""

# Read the Example1.txt
example1 = "C:/developer/phd/Python for Data Science/lab_files/resources/data/Example1.txt"
file1 = open(example1, "r")

# Print the path of file
file1.name

# Print the mode of file, either 'r' or 'w'
file1.mode

# Read the file
FileContent = file1.read()
FileContent

# Print the file with '\n' as a new line
print(FileContent)

# Type of file content
type(FileContent)

# Close file after finish
file1.close()

"""A Better Way to Open a File¶
Using the with statement is better practice, 
it automatically closes the file even if the code encounters an exception.
 The code will run everything in the indent block then close the file object."""
 
# Open file using with
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

"""The file object is closed, you can verify it by running the following cell:"""
# Verify if the file is closed
file1.closed

# See the content of file
print(FileContent)

# Read first four characters
with open(example1, "r") as file1:
    print(file1.read(4))

# Read certain amount of characters
with open(example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))

# Read one line
with open(example1, "r") as file1:
    print("first line: " + file1.readline())

# Iterate through the lines
with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1;

# Read all lines and save as a list
with open(example1, "r") as file1:
    FileasList = file1.readlines()



