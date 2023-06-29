# Declare your age as integer variable
from time import perf_counter
from turtle import width


age = int(30)

# Declare your height as a float variable
height = float(1.67)

# Declare a variable that store a complex number
complex = complex(1.34)

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h). # noqa: E501

b, h = 200, 100

area = 0.5 * (b * h)

print("Area of triangle is ", area)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c). # noqa: E501

""" a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: ")) """

a, b, c = 4,5,6

perimeter = a + b + c
print("Perimeter: ", perimeter)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width)) # noqa: E501

length, width = 10,5

area = length * width
perimeter = 2 * (length + width)

print("Area: ", area)
print("Perimeter: ", perimeter)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14. # noqa: E501

pi, r = 3.14, float(5)

area = pi * (r ** 2)
circumference = 2 * pi * r

print("Area: ", area)
print("Circumference: ", circumference)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2

x_intercept = float(3)

y_intercept = (2*x_intercept) - 2

print(f"Valor de x es {x_intercept} y de y es {y_intercept}. Por ende la pendiente es {y_intercept}")

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10) # noqa: E501
# Euclidean distance: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
x1,x2,y1,y2 = 2,6,2,10

m = (y2 - y1)/(x2 - x1)
euclidean_distance = (((x2 - x1)**2) + ((y2 - y1)**2)) ** 0.5

print("Pendiente: ", m)
print("Euclidean distance: ", euclidean_distance)

# Equation: y = 2x - 2

slope = 2
y_intercept = -2
x_intercept = (0 - y_intercept) / slope

print("Slope (m):", slope)
print("Y-intercept (b):", y_intercept)
print("X-intercept:", x_intercept)


# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0. # noqa: E501

x = -3

y = (x**2) + (6*x) + 9

print("Value (y):",y)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
pyt = "Python"
dra = "Dragon"

print("Value (python):", len(pyt))
print("Dragon (python):", len(dra))
print(pyt == dra)

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on in Python", "on" in pyt)
print("on in Dragon", "on" in dra)

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.  # noqa: E501
jargon = "I hope this course is not full of jargon"
print("jargon: ", 'jargon' in jargon)

# There is no 'on' in both dragon and python
print("Not on in Python", "on" not in pyt)
print("Not on in Dragon", "on" not in dra)

# Find the length of the text python and convert the value to float and convert it to string  # noqa: E501
len_pyt = len(pyt)
float_len_pyt = float(len_pyt)
str_len_pyt = str(float_len_pyt)
print(str_len_pyt)


# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?  # noqa: E501
""" x = int(input("Ingrese numero")) """
x= 8

if (x % 2 == 0):
    print("Si es divisible de 2")
else:
    print("No es divisible de 2")

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_div = 7 // 3
print(floor_div)
print(int(2.7))
print(floor_div == int(2.7))

# Check if type of '10' is equal to type of 10
print(type("10") == type(10))  # noqa: E721
print(isinstance("10", str) == isinstance(10, int)) # Buenas prácticas

# Check if int('9.8') is equal to 10
print(int(9.8)) # noqa: E721
print(isinstance(9.8, int) == 10)

# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?  # noqa: E501
hours,rate = 45,30000

""" rate = int(input("Rate per hour: ")) # noqa: E501 """

print("Rate: ", rate * hours) # noqa: E501

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years  # noqa: E501

life = 100

minutes = 60
hours = minutes * 60
day = hours * 24
year_365 = day * 365

print("Seconds life: ", year_365 * life)
