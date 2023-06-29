### Loops ###

# While 

my_condition = 0

while my_condition <= 10:
    print(my_condition) # 0 a 9
    my_condition += 2
else: # Opcional
    print("Mi condición es mayor que 10") #

print("La ejecucion continúa")

while my_condition <= 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es 15")
        break
    print(my_condition)

# For

my_list = [30, 45, 23, 17, 62, 40, 88, 56]

for element in my_list:
    print(element) # [30, 45, 23, 17, 62, 40, 88, 56]

my_tuple = ("Gerard", "Bourguett", 30, 1.65)

for element in my_tuple:
    print(element) # Gerard, Bourguett, 30, 1.65

my_set = {"Gerard", "Bourguett", 30, 1.65}

for element in my_set:
    print(element) # 1.65, 30, Gerard, Bourguett

my_dict = {"Nombre": "Gerard", "Apellido": "Bourguett", "Edad": 30, "Estatura": 1.65}

for element in my_dict:
    print(element) # Nombre, Apellido, Edad, Estatura
else:
    print("El bucle ha finalizado")

for element in my_dict:
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta")
else:
    print("El bucle ha finalizado")


for element in my_dict.values():
    print(element) # Gerard, Bourguett, 30, 1.65