### Lists ###

my_list = list()
my_other_list = []

print(len(my_list)) # 0

my_list = [30, 29, 41, 51, 52, 53, 54, 55]

print(len(my_list)) # 8

my_other_list = [30, 1.65, "Gerard", "Bourguett"]

print(len(my_other_list),my_other_list, type(my_other_list)) #4 [30, 1.65, 'Gerard', 'Bourguett'] <class 'list'>  # noqa: E501

### [x >= 0 ] = buscará de izquierda a derecha // [x < 0] = buscará de derecha a izquierda  # noqa: E501

print(my_other_list[0]) # 30
print(my_other_list[1]) # 1.65
print(my_other_list[-1]) # Bourguett
print(my_other_list.count(30)) # 1

name, height, age, surname = my_other_list

print(name) # 30

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]  # noqa: E501

print(name, height, age, surname) # Gerard 1.65 30 Bourguett

print(my_list + my_other_list) # [30, 29, 41, 51, 52, 53, 54, 55, 30, 1.65, 'Gerard', 'Bourguett']  # noqa: E501

my_other_list.append("Calendario")
print(my_other_list) # [30, 1.65, 'Gerard', 'Bourguett', 'Calendario']

my_other_list.insert(1, "Caballito")
print(my_other_list) # [30, 'Caballito', 1.65, 'Gerard', 'Bourguett', 'Calendario']

my_other_list[1] = "Calendario 2"
print(my_other_list)  # [30, 'Calendario 2', 1.65, 'Gerard', 'Bourguett', 'Calendario']

my_other_list.remove("Calendario") 
print(my_other_list) # [30, 'Caballito', 1.65, 'Gerard', 'Bourguett']

my_list.remove(30) 
print(my_list) # [29, 41, 51, 52, 53, 54, 55]

print(my_list.pop()) # 55 (remueve el 55 y lo muestra en pantalla)
print(my_list) # [29, 41, 51, 52, 53, 54]

print(my_list.pop(2)) # 51

my_list = [30, 29, 41, 53, 55, 13, 44, 75]
my_pop = my_list.pop(2) # Guarda el 41 en una variable
print(my_pop) # 41
print(my_list) # [30, 29, 53, 55, 13, 44, 75]

del my_list[2]
print(my_list) # [30, 29, 55, 13, 44, 75]

my_new_list = my_list.copy()

my_list.clear() # Limpia la lista
print(my_list) # []
print(my_new_list) # [30, 29, 55, 13, 44, 75]
my_new_list.reverse()
print(my_new_list) # [75, 44, 13, 55, 29, 30] No se puede ejecutar reverse directo desde print  # noqa: E501

my_new_list.sort()
print(my_new_list) # [13, 29, 30, 44, 55, 75]

print([1, 2, 3, 4, 5, 6, 7, 8, 9]) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list = "Hola Python"
print(my_list) # Hola Python
print(type(my_list)) # <class 'str'>




