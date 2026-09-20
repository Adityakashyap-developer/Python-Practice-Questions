#isinstance() function is used to check if an object is an instance of a specific class or a subclass thereof. It returns True if the object is an instance of the specified class, and False otherwise.

x = "shreee"
print(isinstance(x, str))
y = 25
print(isinstance(y, int))
z = 25.5
print(isinstance(z, float))
a1 = [1, 2, 3]
print(isinstance(a1, list))
a2 = (1, 2, 3)
print(isinstance(a2, tuple))
a3 = {1, 2, 3}
print(isinstance(a3, set))
a4 = {"name": "shreee", "age": 25}
print(isinstance(a4, dict)) 
a5 = True
print(isinstance(a5, bool))
a6 = 45
print(isinstance(a6, str))  # False, because a6 is an integer, not a string 


#sys.getsizeof() isto find the memory size (in bytes) of an objectin Python .

import sys

x = "shreee"
y = 25
z = 25.5
a1 = [1, 2, 3]
a2 = (1, 2, 3)
a3 = {1, 2, 3}
a4 = {"name": "shreee", "age": 25}
a5 = True

print(sys.getsizeof(x))  # Size of string "shreee"
print(sys.getsizeof(y))  # Size of integer 25
print(sys.getsizeof(z))  # Size of float 25.5
print(sys.getsizeof(a1))  # Size of list [1, 2, 3]
print(sys.getsizeof(a2))  # Size of tuple (1, 2, 3)
print(sys.getsizeof(a3))  # Size of set {1, 2, 3}
print(sys.getsizeof(a4))  # Size of dictionary {"name": "shreee", "age": 25}
print(sys.getsizeof(a5)) # Size of boolean True


# Using f-string for formatting

x = "aditya"
y = 25
print(f"my name is {x} and my age is {y}")  


# bit - A bit is the smallest unit of data. It can have only 2 values: 0 or 1. 
# byte - A byte is a group of 8 bits. 
# 
# 1 Byte = 8 bits


x = 1
y = 0
print(x)
print(y)



