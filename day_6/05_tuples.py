### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (30, 1.65, "Gerard", "Bourguett", "Gerard", "React", "Javascript")
print(my_tuple) # (30, 1.65, 'Gerard', 'Bourguett', 'Gerard')
print(type(my_tuple)) # <class 'tuple'>

print(my_tuple[0]) # 30
print(my_tuple[-1]) # Bourguett

print(my_tuple.count("Gerard")) # 2
print(my_tuple.index("Gerard")) # 2

# my_tuple[1] = 1.70 TypeError: 'tuple' object does not support item assignment
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# print(my_sum_tuple[3,6]) TypeError: tuple indices must be integers or slices, not tuple
print(my_sum_tuple[3:6]) # ('Bourguett', 'Gerard', 'React')

my_tuple = list(my_tuple)
print(type(my_tuple)) # <class 'list'>

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined