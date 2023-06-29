# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(x, y):
    print(x + y)

add_two_numbers(1, 2)

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_circle(r):
    area = 3.14 * (r ** 2)
    print(area)

area_circle(5)

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*nums):
    suma = 0
    for num in nums:
        if isinstance(num, (int, float)):
            suma += num
        else:
            print("No se pueden sumar elementos que no son números")
            return
    return suma

print(add_all_nums(2,3,5))

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def celsius_to_fahrenheit(c):
    far = (c * (9/5)) + 32
    return far

print(celsius_to_fahrenheit(17))

def farenheit_to_celsius(f):
    cel = (f - 32) * (5/9)
    return cel

print(farenheit_to_celsius(90))

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.lower() # Convertir a minusculas

    dict_months = {
        'diciembre': 'Verano',
        'noviembre': 'Primavera',
        'octubre': 'Primavera',
        'septiembre': 'Primavera',
        'agosto': 'Invierno',
        'julio': 'Invierno',
        'junio': 'Invierno',
        'mayo': 'Otoño',
        'abril': 'Otoño',
        'marzo': 'Otoño',
        'febrero': 'Verano',
        'enero': 'Verano',
    }

    if month in dict_months:
        return dict_months[month]
    else: 
        return 'Mes inválido'

print(check_season("Enero"))

# Write a function called calculate_slope which return the slope of a linear equation
# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).