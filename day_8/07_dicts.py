### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict)) # <class 'dict'>
print(type(my_other_dict)) # <class 'dict'>

my_dict = {"Nombre" : "Gerard", "Apellidos" : "Bourguett", "Edad" : 30, "Lenguajes" : {"Python", "React", "HTML"}, 2: 1.65, "Calle" : "Falsa 123"}  # noqa: E501

my_other_dict = {"Nombre" : "Gerard", "Apellidos" : "Bourguett", "Edad" : 30, 1: "Python"}  # noqa: E501

print(my_other_dict) # {'Nombre': 'Gerard', 'Apellidos': 'Bourguett', 'Edad': 30, 1: 'Python'}  # noqa: E501
print(my_dict) #  {'Nombre': 'Gerard', 'Apellidos': 'Bourguett', 'Edad': 30, 'Lenguajes': {'React', 'Python', 'HTML'}, 2: 1.65, 'Calle': 'Falsa 123'  # noqa: E501
print(len(my_dict)) # 6, cuenta las claves y no la cantidad de valores
print(my_dict["Nombre"]) # Gerard

my_dict["Apellidos"] = "Bourguett Cantillana" 
print(my_dict) # {'Nombre': 'Gerard', 'Apellidos': 'Bourguett Cantillana', 'Edad': 30, 'Lenguajes': {'React', 'Python', 'HTML'}, 2: 1.65, 'Calle': 'Falsa 123'}  # noqa: E501

my_dict["Calle"] = "Calle Falsa 123"
print(my_dict) #  {'Nombre': 'Gerard', 'Apellidos': 'Bourguett Cantillana', 'Edad': 30, 'Lenguajes': {'React', 'Python', 'HTML'}, 2: 1.65, 'Calle': 'Calle Falsa 123'}  # noqa: E501

del my_dict["Calle"]
print(my_dict) # {'Nombre': 'Gerard', 'Apellidos': 'Bourguett Cantillana', 'Edad': 30, 'Lenguajes': {'React', 'HTML', 'Python'}, 2: 1.65}  # noqa: E501

print("Gerard" in my_dict) # False porque estamos buscando por clave y no por valor
print("Apellidos" in my_dict) # True

print(my_dict.items()) # dict_items([('Nombre', 'Gerard'), ('Apellidos', 'Bourguett Cantillana'), ('Edad', 30), ('Lenguajes', {'HTML', 'React', 'Python'}), (2, 1.65)])  # noqa: E501

print(my_dict.keys()) # dict_keys(['Nombre', 'Apellidos', 'Edad', 'Lenguajes', 2])
print(my_dict.values()) # dict_values(['Gerard', 'Bourguett Cantillana', 30, {'React', 'HTML', 'Python'}, 1.65])  # noqa: E501

my_list = {"Nombre", 1, "Piso"}

print(my_dict.fromkeys(("Nombre", 0))) # {'Nombre': None, 0: None} Crea un dict sin valores  # noqa: E501
thisdict = dict.fromkeys(my_dict, 0)
print(thisdict) # {'Nombre': 0, 'Apellidos': 0, 'Edad': 0, 'Lenguajes': 0, 2: 0}
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict) # {'Piso': None, 1: None, 'Nombre': None}
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict)) # {'Nombre': None, 1: None, 'Piso': None}
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict)) # {'Nombre': None, 'Apellidos': None, 'Edad': None, 'Lenguajes': None, 2: None}  # noqa: E501
my_new_dict = dict.fromkeys(my_dict, "Gerard")
print((my_new_dict)) # {'Nombre': ('Gerard', 'Bourguett'), 'Apellidos': ('Gerard', 'Bourguett'), 'Edad': ('Gerard', 'Bourguett'), 'Lenguajes': ('Gerard', 'Bourguett'), 2: ('Gerard', 'Bourguett')}  # noqa: E501

my_values = my_new_dict.values()
print(type(my_values)) # <class 'dict_values'>

print(my_new_dict.values()) # dict_values(['Gerard', 'Gerard', 'Gerard', 'Gerard', 'Gerard'])  # noqa: E501
print(list(my_new_dict.values())) # ['Gerard', 'Gerard', 'Gerard', 'Gerard', 'Gerard']
print(tuple(my_new_dict)) # ('Nombre', 'Apellidos', 'Edad', 'Lenguajes', 2)
print(set(my_new_dict)) # {'Nombre', 'Lenguajes', 2, 'Edad', 'Apellidos'}
print(list(dict.fromkeys(list(my_new_dict.values())).keys())) # ['Gerard']