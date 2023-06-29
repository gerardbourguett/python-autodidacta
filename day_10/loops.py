# Iterate 0 to 10 using for loop, do the same using while loop.

count = 0

while count <= 10:
    print(count)
    count += 1

# Iterate 10 to 0 using for loop, do the same using while loop.

count = 10

while count >= 0:
    print(count)
    count = count - 1

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:

count = 0
parafrase = "#"

while count < 7: 
    print(parafrase)
    parafrase += "#"
    count += 1

# Use nested loops to create the following:

y = 5
t = 5

for i in range(y):
    for j in range(t):
        print("* ", end="")
    print()

# Print the following pattern:

factor = 10

for i in range(factor + 1):
    print(f"{i} x {i} = {i ** 2}")

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.  # noqa: E501

my_list = ['Python', 'Numpy','Pandas','Django', 'Flask']

for element in range(len(my_list)):
    print(my_list[element])

# Use for loop to iterate from 0 to 100 and print only even numbers

cien = 100

for element in range(cien + 1):
    if element % 2 == 0:
        print(element)

# Use for loop to iterate from 0 to 100 and print only odd numbers

cien = 100

for element in range(cien + 1):
    if element % 2 != 0:
        print(element)

# Level 2

# Use for loop to iterate from 0 to 100 and print the sum of all numbers.

cien = 101
contador = 0

for element in range(cien):
    contador += element
print(contador)

par = 0
impar = 0

for element in range(cien):
    if element % 2 == 0:
        par += element
    else:
        impar += element

print(par, impar)