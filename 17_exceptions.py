### Exception Handling ###

numberOne = 6
numberTwo = 1

numberTwo = "Secuestro"

# try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:  # noqa: E722
    print("Se ha producido un error") # Se ha producido un error

# try except else

numberOne = 6
numberTwo = 1

try:
    print(numberOne + numberTwo) # 7
    print("No se ha producido un error") # No se ha producido un error
except:  # noqa: E722
    print("Se ha producido un error")
else:
    print("La ejecución continúa correctamente")

# try except else finally

numberOne = 2
numberTwo = 4

try:
    print(numberOne + numberTwo) # 6
    print("No se ha producido un error") # No se ha producido un error
except:  # noqa: E722
    print("Se ha producido un error")
else:
    print("La ejecución continúa correctamente") # La ejecución continúa correctamente
finally:
    print("La ejecución continúa") # La ejecución continúa

# Exceptions por tipo

numberOne = 'Hioli'
numberTwo = 3

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError:
    #Se ejecutará solo si ocurre una excepción TypeError
    print("Se ha producido un TypeError") # Se ha producido un TypeError
except ValueError:
    print("Se ha producido un ValueError") 

# Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as exception:
    print(exception) # can only concatenate str (not "int") to str

# Captura Value Error

try:
    numberOne = int(numberOne)
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError") # Se ha producido un ValueError

