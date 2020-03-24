# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 01:54:47 2020
STRING OPERATIONS
@author: ahmed
"""
# Use quotation marks for defining string
"Michael Jackson"

# Assign string to variable
Name = "Michael Jackson"
Name
# Print the first element in the string
print(Name[0])
# Print the last element in the string
print(Name[-1])
len(Name)
Name[8:12]
Name[::2]
Name[0:5:2]

3 * "Michael Jackson"

Name = "Michael Jackson"
Name = Name + " is the best"
Name

# r will tell python that string will be display as raw string
print(r" Michael Jackson \ is the best" )
print(" Michael Jackson \\ is the best" )

# Convert all the characters in string to upper case
A = "Thriller is the sixth studio album"
print("before upper:", A)
B = A.upper()
print("After upper:", B)

# Replace the old substring with the new target substring is the segment has been found in the string
A = "Michael Jackson is the best"
B = A.replace('Michael', 'Janet')
B

# Find the substring in the string. Only the index of the first elment of substring in string will be the output
Name = "Michael Jackson"
Name.find('el')

name = 'Lizz'
print(name[0:2])

var = '01234567'
 print(var[::2])
'1'+'2'
