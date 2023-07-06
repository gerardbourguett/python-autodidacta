# Escribe un programa en Python que muestre por consola los números del 1 al 100,
# sustituyendo ciertos números por palabras específicas según las siguientes reglas:
# - Si un número es múltiplo de 3, se imprimirá la palabra "fizz" en su lugar.
# - Si un número es múltiplo de 5, se imprimirá la palabra "buzz" en su lugar.
# - Si un número es múltiplo tanto de 3 como de 5, se imprimirá la palabra "fizzbuzz" en su lugar.  # noqa: E501
# Cada número o palabra se imprimirá en una nueva línea.


def fizzbuzz():
    secuencia = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            secuencia.append("fizzbuzz")
        elif i % 3 == 0:
            secuencia.append("fizz")
        elif i % 5 == 0:
            secuencia.append("buzz")
        else:
            secuencia.append(str(i))
    print(secuencia)


fizzbuzz()

""" /*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */ """


texto_original = "Python"


def hacker(texto_original):
    leet = {
        "a": "4",
        "b": "I3",
        "c": "[",
        "d": ")",
        "e": "3",
        "f": "|=",
        "g": "&",
        "h": "#",
        "i": "1",
        "j": ",_|",
        "k": ">|",
        "l": "£",
        "m": "/\/\ ",
        "n": "^/",
        "o": "0",
        "p": "|*",
        "q": "(_,)",
        "r": "I2",
        "s": "5",
        "t": "7",
        "u": "(_)",
        "v": "\/",
        "w": "\/\/",
        "x": "><",
        "y": "j",
        "z": "2",
    }

    texto_leet = ""

    for letra in texto_original:  # Va a recorrer el texto original letra por letra
        if letra in leet:
            texto_leet += leet[
                letra
            ]  # Si letra está en el diccionario, se añade a la cadena de texto leet y su resultado en el dict  # noqa: E501
        else:
            texto_leet += (
                letra  # Si letra no está en el diccionario, se añade a la cadena
            )

    print(texto_leet)


hacker(texto_original)


""" /*
 * Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */ """  # noqa: E501


def anagrama(palabra1, palabra2):
    if palabra1.lower() == palabra2.lower():
        return True
    """ palabra1 = list(palabra1.lower())
    palabra2 = list(palabra2.lower())
    return palabra1.sort() == palabra2.sort() """
    return sorted(palabra1.lower()) == sorted(palabra2.lower())


print(anagrama("secuestro", "Orsteuces"))

""" /*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */ """


""" def fibonacci(n):
    sequence = [0, 1]  # Inicializar los primeros dos números de la secuencia

    # Utilizar una comprensión de lista para generar los siguientes números de Fibonacci
    [sequence.append(sequence[-1] + sequence[-2]) for _ in range(2, n)]

    return sequence


# Ejemplo de uso
n = 50
fibonacci_sequence = fibonacci(n)
print(fibonacci_sequence) """


def fibonacci(n):
    secuencia = [0, 1]

    for i in range(2, n + 1):
        siguiente = secuencia[i - 1] + secuencia[i - 2]
        secuencia.append(siguiente)

    print(secuencia)


fibonacci(50)


""" def fibonacci():
    prev = 0
    next = 1
    for index in range(0, 51):
        print(prev)
        fib = prev + next
        prev = next
        next = fib


fibonacci() """

""" /*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */ """


""" def primos():
    for i in range(1, 101):
        primo = True
        for j in range(2, i):
            if i % j == 0:
                primo = False
                break
        if primo == True:
            print(i) """


def primos():
    secuencia = []
    for i in range(2, 101):
        primo = True
        for j in range(2, i):
            if i % j == 0:
                primo = False
                break
        if primo is True:
            secuencia.append(i)
    print(secuencia)


primos()

""" /*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */ """


def area_poligono(poligono):
    poligono = poligono.lower()
    if poligono == "triangulo":
        base = 5
        altura = 10
        """ base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: ")) """
        area = (base * altura) / 2
        print(f"El área del triángulo es: {area}")
    elif poligono == "cuadrado":
        base = float(input("Ingrese la base del cuadrado: "))
        area = base * base
        print(f"El área del cuadrado es: {area}")
    elif poligono == "rectángulo":
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = base * altura
        print(f"El área del rectángulo es: {area}")


area_poligono("Triangulo")

""" /*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */ """

# Forma rápida
""" def invertir_cadena(cadena):
    return cadena[::-1] """


def invertir_cadena(cadena):
    reversed_text = ""
    for letra in cadena:  # Va a recorrer el texto original letra por letra
        reversed_text = (
            letra + reversed_text
        )  # Va añadiendo la letra al final de la cadena  # noqa: E501
    return reversed_text


print(invertir_cadena("Hola mundo"))

""" /*
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
 */ """


def text_to_morse(text):
    lang_morse = {  # noqa: F841
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...",
        "W": ".--",
        "X": "-.-",
        "Y": "-.-",
        "Z": "--.-",
        " ": " ",
    }

    text = text.upper()
    conv = ""
    for letra in text:  # Va a recorrer el texto original letra por letra
        if letra in lang_morse:
            conv += lang_morse[letra] + " "
        else:
            conv += letra  # Si letra no está en el diccionario, se añade a la cadena
    return conv


print(text_to_morse("Hola mundo"))
