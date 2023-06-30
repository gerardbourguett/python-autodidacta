### Functions ###

def my_function ():
    print("Esto es una funcion")

my_function () # Esto es una funcion

def suma(x, y):
    sum = x+y
    print(f"Suma: {x} + {y} = {sum}") # Suma: 2.4 + 3.25 = 5.65
    print(x + y) # 5.65

suma(2.4, 3.25) # Suma: 2.4 + 3.25 = 5.65 \n 5

def suma_con_return(first_value, second_value):
    return first_value + second_value

my_result = suma_con_return(25,54)
print(my_result) # 79

def print_name(name, surname):
    print(f"{name} {surname}")

print_name("Gerard", "Bourguett") # Gerard Bourguett
print_name(name = "Bourguett", surname = "Gerard") # Bourguett Gerard

