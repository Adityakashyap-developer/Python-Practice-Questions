# 1. Write a program to declare a variable and print its value.
x = 25
print(x)
y = "Jhon"
print(y)



# 2. Take user input and store it in a variable, then print it.
your_name = input("Enter your name: ")
print(your_name)


# 3. Swap two variables without using a third variable.
x = 25
z = 30
x, z = z, x
print(x)
print(z)


# 4. Check the data type of a variable using type().
x = 25
print(type(x))
y = "Jhon"
print(type(y))


# 5. Convert a string to an integer.
x = "25"
x = int(x) 
print(x)
print(type(x))

# 6. Convert an integer to a string.
x = 25
x = str(x)
print(x)
print(type(x))


# 7. Convert a string to a float.
x = "25.5"
x = float(x)
print(x)
print(type(x))


# 8. Convert a float to an integer.
x = 25.5
x = int(x) 
print(x)
print(type(x))


# 9. Check if a variable is an integer using isinstance().
x = 25
print(isinstance(x, int))               
"""isinstance main job is to check whether an object (variable) is of a particular data type (like int, str, list) or class."""


# 10. Create a variable with a boolean value and print its type.
x = True
print(type(x))

# 11. Write a program that takes two numbers as input and prints their sum.
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
sum = int(num1) + int(num2)
print(sum)


# 12. Assign multiple variables in a single line (e.g., a, b, c = 1, 2, 3).
a , b , c = 1 , 2 , 3
print(a)
print(b)
print(c)


# 13. Assign the same value to multiple variables in one line.
x = y = z = 10
print(x)
print(y)
print(z)


# 14. Find the size (in bytes) of a variable using sys.getsizeof().
import sys
x = 25
y = "character"
print(sys.getsizeof(x))
print(sys.getsizeof(y))


# 15. Print the ASCII value of a character using ord().
print(ord('A'))  

# 16. Print the character for a given ASCII value using chr().
print(chr(65))  


# 17. Check whether a variable is None.
x = None
print(x is None)


# 18. Take a user's name and age as input and print a formatted sentence.
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
print(f"My name is {user_name} and I am {user_age} years old.")


# 19. Convert a boolean value to an integer.
x = True
x = int(x)
print(x)


# 20. Convert an integer to a boolean.
x = 1
x = bool(x)
print(x)


# 21. Demonstrate the difference between is 'and' and == for two variables.
a = 10
b = 10
print(a == b)
print(a and b)


# 22. Create a complex number variable and print its real and imaginary parts.
z =  5+7j
print("Real:" , z.real)
print("Imaginary:" , z.imag)


# 23. Write a program to check if a number is positive, negative, or zero.
n = int(input("Enter a number :"))
if n > 0:
    print("Positive")
elif n < 0:
    print("Nagetive")
else:
    print("Zero")


# 24. Take temperature in Celsius as input and convert it to Fahrenheit.
c = float(input('Enter temperature in celsius :'))
f = (c * 5/9) + 32
print("Fahrenheit:" , f)


# 25. Take temperature in Fahrenheit as input and convert it to Celsius.
f = float(input('Enter temperature in fahrenheit :'))
c = (f-32) * 5/9
print("Celsius :" , c)


# 26. Calculate the area of a rectangle using variables for length and width.
length = float(input("Enter length:"))
width = float(input("Enter width:"))
area =  length * width 
print("Area is:" , area)


# 27. Calculate the perimeter of a rectangle using variables.
length = float(input("Enter length:"))
width = float(input("Enter width:"))
perimeter = 2*(length + width)
print(perimeter)


# 28. Calculate simple interest using principal, rate, and time as variables.
principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))
si = (principal * rate * time) / 100
print("Simple Interest:", si)


# 29. Write a program to find the largest of two numbers using variables.
A = float(input("Enter first number:"))
B = float(input("Enter second number:"))
print("largest" , max(A,B))


# 30. Write a program to find the smallest of two numbers using variables.
A = float(input("Enter first number:"))
B = float(input("Enter second number:"))
print("largest" , min(A,B))


# 31. Store a list, a tuple, and a dictionary in variables and print their types.
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_dict = {"a": 1, "b": 2}

print(type(my_list))
print(type(my_tuple))
print(type(my_dict))


# 32. Take a decimal number and separate its integer and fractional parts.
n = float(input("Enter decimal number:"))
integer = int(n)
fraction = n - integer
print("Integer part:", integer)
print("Fractional part:", fraction)


# 33. Write a program to check if two variables point to the same object using id().
a = [1, 2, 3]
b = a

print(id(a))
print(id(b))
print(a is b)


# 34. Create a variable with a very large integer and print it (demonstrate no overflow in Python).
n = 99999999999999999999999999999999999999999999999999999
print(n)


# 35. Write a program to reverse the values of two numeric variables mathematically (without a third variable, using arithmetic).
a = 10
b = 20

a = a + b #30
b = a - b
a = a - b

print(a)
print(b)


# 36. Take a user's height in centimeters and convert it to feet and inches.
height_cm = float(input("Enter height in cm:"))
total_inches = height_cm / 2.54
feet = int(total_inches // 12 )
inches = total_inches %  12

print(feet)
print(inches)


# 37. Take principal amount, years, and rate to calculate compound interest.
# Ans. Use the formula and plug in the values, just like we did for the 28th question; look up the formula on Google.


# 38. Create a variable holding a fraction using the fractions module.
from fractions import Fraction 
f = Fraction(3,4)
print(f)


# 39. Write a program to check whether a variable is mutable or immutable (compare list vs tuple behavior).
my_list = [1,2,3,4]
my_tuple = ( 1,2,3)

my_list.append(4)
print("List:", my_list)
print("Tuple:", my_tuple)  #Convert the tuple into a list when we add remove update.


# 40. Take marks of 3 subjects as input and calculate the average.
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))

average = (m1 + m2 + m3) / 3
print("Average:", average)


# 41. Write a program to calculate BMI using weight and height variables.
#            BMI = weight (kg) / height (m)²
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

print("BMI:", bmi)


# 42. Take a number and check if it's even or odd using a variable.
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 43. Create a variable and reassign it to a different data type (demonstrate dynamic typing).
x = 10
print(x, type(x))

x = "Hello"
print(x, type(x))

x = 3.14
print(x, type(x))


# 44. Write a program to calculate the number of seconds in a given number of hours (input by
# user).
hours = float(input("Enter hours: "))
seconds = hours * 60 * 60
print("Seconds:", seconds)


# 45. Take a value in kilometers and convert it to miles.
km = float(input("Enter kiloneter:"))
miles = km * 0.621371
print(miles)


# 46. Take a value in miles and convert it to kilometers.
miles = float(input("Enter miles:"))
km = miles * 1.60934
print(km)


# 47. Take two variables holding numbers and print their sum, difference, product, and quotient.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)


# 48. Write a program to check the memory address of a variable using id() before and after reassignment.
x = 10
print("Before reassignment:", id(x))
x = 20
print("After reassignment:", id(x))


# 49. Write a program to declare variables of every built-in Python data type and print each type().
a = 10                  # int
b = 3.14                # float
c = 2 + 3j              # complex
d = True                 # bool
e = "Hello"              # str
f = [1, 2, 3]            # list
g = (1, 2, 3)            # tuple
h = {1, 2, 3}            # set
i = {"a": 1, "b": 2}     # dict
j = range(5)             # range
m = frozenset([1, 2, 3]) # frozenset
n = None                 # NoneType

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(m))
print(type(n))


# 50. Write a program to demonstrate implicit type conversion when adding an int and a float.
a = 10
b = 3.5
result = a + b

print("Result:", result)
print("Type:", type(result))

