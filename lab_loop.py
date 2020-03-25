# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 00:07:36 2020
@author: 1426391
Loop
"""
# Use the range
range(3)

# For loop example
""""The code in the indent is executed N times, 
each time the value of i is increased by 1 for every execution.
 The statement executed is to print out the value in the list at index i as shown here:""""
dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])    
for i in range(0, 8):
    print(i)
for year in dates:  
    print(year)  

# Use for loop to change the elements in list
squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'weight'
    print("After square ", i, 'is',  squares[i])

# Loop through the list and iterate on both index and element value
squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)

# While Loop Example
dates = [1982, 1980, 1973, 2000]

i = 0
year = 0

while(year != 1973):
    year = dates[i]
    i = i + 1
    print(year)

print("It took ", i ,"repetitions to get out of loop.")


















