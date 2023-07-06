### Lambdas ###

sum = lambda first_value, second_value: first_value + second_value

print(sum(1, 2))  # 3

multiply = lambda first_value, second_value: first_value * second_value - 3

print(multiply(2, 4))  # 5


def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value


print(sum_three_values(6)(2, 4))  # 12


def sum_value_and_lambda(
    value,
):
    return lambda first_value, second_value: first_value + second_value + value
