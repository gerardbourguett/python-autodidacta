### Condicionals ###


a = 3

my_condition = True

if my_condition:
    print("Se ejecuta la condición del if")
    
print("la ejecución continúa")

my_condition == 5 * 2

if my_condition == 10:
    print("ta bien") # ta bien
else:
    print("No se ejecuta")

if my_condition > 10 and my_condition < 20:
    print("Es mayor de 10")
else:
    print("Es menor o igual 20") # Es menor o igual 20

my_condition == 5 * 3 # 15

if my_condition == 10:
    print("ta bien") 
else:
    print("No se ejecuta") # No se ejecuta

if my_condition > 10 and my_condition < 20:
    print("Es mayor de 10") # Es mayor de 10
else:
    print("Es menor o igual 20")
    
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero') # A is zero

a = 3
print("A is a positive") if a > 0 else print("A is negative") # A is a positive
