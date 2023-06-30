""" Operadores matemáticos """

print(3 + 4)  # Suma, imprimirá 7
print(10 - 5)  # Resta, imprimirá 5
print(3 * 6)  # multiplica, imprimirá 18
print(3 / 4)  # Divide, imprimirá 0.75
print(10 % 2)  # Calcula el resto, útil para verificar pares (Imprimirá 0)
print(
    10 // 3
)  # División que acaba aproximada a un entero, es como decir cuantas veces cabe Y en X. En este caso imprimirá 3  # noqa: E501
print(2**3)  # Potencias, es 2 elevado a 3. Imprimirá 8
print(2**3 + 3 - 7 / 1 // 5)  # Imprimirá 10

print("Hola " + "Python " + "¿Que onda?")  # Hola Python ¿Que onda?
print("Hola " + str(5))  # Hola 5, forzamos que 5 sea un string y no un int
print("Hola " * 5)  # Hola Hola Hola Hola Hola
print("Hola " * (2**3))  # Hola Hola Hola Hola Hola Hola Hola Hola

my_float = 2.5 * 2  # 5.0

print(
    "Hola " * int(my_float)
)  # Hola Hola Hola Hola Hola, al cambiar a INT deja de valer 5.0 y pasa a valer 5 entero.  # noqa: E501

""" Operadores comparativos """

print(3 > 4)  # False
print(3 < 4)  # True
print(3 >= 4)  # False
print(3 <= 4)  # True
print(3 == 4)  # False
print(3 != 4)  # True

"""Comparativa de caracteres (Cuenta)"""

print("Hola" > "Python")  # False
print("Hola" < "Python")  # True
print("aaaa" < "abaa")  # Ordena alfabéticamente por ASCII, Imprimirá True
print(len("aaaa") > len("abaa"))  # Cuenta caracteres. Imprimirá False
print("Hola" <= "Python")  # true
print("Hola" >= "Python")  # False
print("Hola" == "Hola")  # True
print("Hola" != "Hola")  # False


""" Operadores Lógicos """

print(3 < 4 and "Hola" > "Python")  # False (True AND False = False)
print(3 < 4 or "Hola" > "Python")  # True (True OR False = True)
print(3 < 4 and "Hola" < "Python")  # True (True AND True = True)
print(3 < 4 or "Hola" > "Python")  # True (True OR False = True)
print(
    3 < 4 or ("Hola" > "Python" and 4 == 4)
)  # True (True OR (False and True = False) = True)
print(not (3 > 4))  # True
