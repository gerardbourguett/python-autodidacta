### Higher order functions ###

# Higher order functions are functions that take functions as arguments or return functions.  # noqa: E501


def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sum_two_values_and_add_value(x, y, f_sum):
    return f_sum(x + y)


print(sum_two_values_and_add_value(5, 2, sum_one))  # 8
print(sum_two_values_and_add_value(5, 2, sum_five))  # 12
# print(sum_two_values_and_add_value(5, 2, 10))  # Dara error por f_sum en la funcion sum_two_values_and_add_value  # noqa: E501

### Closures ###


def sum_ten():
    ten = 10

    def add(num):
        return num + ten

    return add


closure_result = sum_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20


def sum_ten_and_add(value):
    ten = 10

    def add(num):
        return value + num + ten

    return add


closure_result = sum_ten_and_add(5)
print(closure_result(10))  # 25
print(sum_ten_and_add(5)(10))  # 25

### Built-in Higher Order Functions ###

# Map

numbers = [1, 2, 3, 4, 5]  # iterable


def square(x):
    return x**2


numbers_squared = map(square, numbers)
print(list(numbers_squared))  # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x: x**2, numbers)
print(list(numbers_squared))  # [1, 4, 9, 16, 25]


def multuply_two(number):
    return number * 2


print(list(map(multuply_two, numbers)))  # [2, 4, 6, 8, 10]
print(list(map(lambda x: x * 2, numbers)))  # [2, 4, 6, 8, 10]

# Filter

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers2 = [16, 15, 14, 13, 12, 11, 10, 9]


def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False


print(list(filter(filter_greater_than_ten, numbers)))  # [11, 12, 13, 14, 15]
print(list(filter(lambda x: x > 10, numbers2)))  # [16, 15, 14, 13, 12, 11]

# Reduce

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def sum_two_values(x, y):
    return x + y


print(reduce(sum_two_values, numbers))  # 120
print(reduce(lambda x, y: x if x > y else y, numbers))  # 15
