### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set)) # <class 'set'>
print(type(my_other_set)) # <class 'dict'>

st = {'item1', 'item2', 'item3', 'item4'}
print(st) # {'item2', 'item3', 'item4', 'item1'}
print(len(st)) # 4

print('item3' in st) # True

my_other_set = {"Gerard", "Bourguett", 30}
print(type(my_other_set)) # <class 'set'>
print(len(my_other_set)) # 3

my_other_set.add("Caballito")

print(my_other_set) # set no es una estructura ordenada, por tanto cada Run no será el mismo orden de valores  # noqa: E501

my_other_set.add("Caballito")

print(my_other_set) # set no permite repetidos

my_other_set.add("Caballito :(")

print(my_other_set) # {'Caballito :(', 'Gerard', 'Caballito', 'Bourguett', 30}

print("Caballito" in my_other_set) # True
print("Gerardo" in my_other_set) # True

my_other_set.remove("Caballito :(")
my_other_set.discard("Caballito :(") # discard() no genera ningún error y simplemente no realiza ninguna acción en ese caso.  # noqa: E501
print(my_other_set) # {'Caballito', 'Gerard', 'Bourguett', 30}

