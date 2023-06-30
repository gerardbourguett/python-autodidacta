### Strings ###

my_string = "Mi string 1"
my_other_string = "My string"

print(my_string + " " + my_other_string)  # Mi string 1 My string

my_new_line_string = "Este es un string\ncon salto de linea"

print(my_new_line_string)
"""Este es un string
con salto de linea"""


my_tab_string = "Este es un string\tcon tabulacion"
print(my_tab_string)  # Este es un string       con tabulación

# Formateo de datos

name, surname, age = "Gerard", "Bourguett", 30

print(
    "Mi nombre es {} {} y mi edad es {}".format(name, surname, age)
)  # Mi nombre es Gerard Bourguett y mi edad es 30  # noqa: E501
print(
    "Mi nombre es %s %s y mi edad es %d" % (name, surname, age)
)  # Mi nombre es Gerard Bourguett y mi edad es 30. %s es string y %d para numeros  # noqa: E501
print(
    "Mi nombre es {name} {surname} y mi edad es {age}"
)  # Mi nombre es {name} {surname} y mi edad es {age} # noqa: E501
print(
    f"Mi nombre es {name} {surname} y mi edad es {age}"
)  # Mi nombre es Gerard Bourguett y mi edad es 30 # noqa: E501


# Desempaquetado de caracteres

language = "Python"
(
    a,
    b,
    c,
    d,
    e,
    f,
) = language  # "Python" tiene seis caracteres, por tanto deben declararse seis variables # noqa: E501

print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n

# Division

language_slice = language[1:3]
print(language_slice)  # yt

language_slice = language[1:]
print(language_slice)  # ython

language_slice = language[-2]
print(language_slice)  # o

language_slice = language[1:2:4]
print(language_slice)  # y

# Reverse

reversed_language = language[:-1]
print(reversed_language)  # Pytho

# Funciones

print(language.capitalize()) # Python
print(language.upper()) # PYTHON
print(language.count("t")) # 1
print(language.isnumeric()) # False
print(language.lower()) # python
print(language.lower().isupper()) # False
print(language.startswith("Py")) # True
print("Py" == "py")