#variables

variable_string = "Variable String"
print(variable_string)

variable_int = 5
print(variable_int)

int_a_string = str(variable_int)
print(int_a_string)
print(type(int_a_string))

variable_bool = False
print(variable_bool)

#Concatenación
print(variable_string, variable_int, variable_bool)

name = input('Nombre: ')
age = input('Edad')

#cambio de tipo
name = 35
age = "Gerard"

print("Mi nombre es ", name, ". Edad: ", age)


#Forzando el tipo
address: str = "Mi direccion"
address = 32
print(address) #Imprimirá 32
print(type(address)) #Imprimirá INT, Python es de tipado débil por lo que no se guarda el forzado anterior sino que se queda con el ultimo tipo escrito- # noqa: E501

