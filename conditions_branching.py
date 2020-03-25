# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 22:53:27 2020

@author: 1426391

CONDITIONS AND BRANCHING
Comparison Operators
Comparison operations compare some value or operand and, based on a condition, they produce a Boolean. When comparing two values you can use these operators:

equal: ==
not equal: !=
greater than: >
less than: <
greater than or equal to: >=
less than or equal to: <=
"""
# Condition Equal
a = 5
a == 6

# Greater than Sign
i = 2
i > 5

# Inequality Sign
i = 2
i != 6

# Inequality Sign
i = 6
i != 6

"ACDC" == "Michael Jackson"
"ACDC" != "Michael Jackson"
'B' > 'A'
'BA' > 'AB'

# Elif statment example
age = 18
#age = 19
if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")

# Condition statement example
album_year = 1983
#album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")

print('do something..')

# Condition statement example
album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("")
print("Do Stuff..")


# Condition statement example
album_year = 1983

if not (album_year == '1984'):
    print ("Album year is not 1984")
