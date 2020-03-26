# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 03:14:56 2020

@author: 1426391
Writing Files
We can open a file object using the method write() to save the text file to a list.
 To write the mode, argument must be set to write w. 
 Let’s write a file Example2.txt with the line: “This is line A”
"""

# Write line to file
with open('C:/developer/phd/Python for Data Science/lab_files/resources/data/Example2.txt', 'w') as writefile:
    writefile.write("This is line A")
    writefile.write("This is line B\n")

# Read file
with open('C:/developer/phd/Python for Data Science/lab_files/resources/data/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
    
# Write a new line to text file
with open('C:/developer/phd/Python for Data Science/lab_files/resources/data/Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")

# Sample list of text
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
Lines
  
# Write the strings in the list to text file
with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
# Append the line to the file
with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line D\n")
    
# Verify if the new line is in the text file
with open('/resources/data/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

# Copy file to another
with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)



















