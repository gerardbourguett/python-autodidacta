### List Comprehensions ###

my_original_list = [35, 24, 62, 52, 38, 30, 17]

my_list = [i for i in my_original_list]
print(my_list) # [35, 24, 62, 52, 38, 30, 17]

my_original_range = range(8)
my_range = [i for i in my_original_range]
print(my_range) # [0, 1, 2, 3, 4, 5, 6, 7]

my_range = [i * 2 for i in range(8)]
print(my_range) # [0, 2, 4, 6, 8, 10, 12, 14]

my_range = [i * i for i in range(8)]
print(my_range) # [0, 1, 4, 9, 16, 25, 36, 49]

def fibonacci(n):
    sequence = [0, 1]  # Inicializar los primeros dos números de la secuencia

    # Utilizar una comprensión de lista para generar los siguientes números de Fibonacci
    [sequence.append(sequence[-1] + sequence[-2]) for _ in range(2, n)]

    return sequence

# Ejemplo de uso
n = 10
fibonacci_sequence = fibonacci(n)
print(fibonacci_sequence)

