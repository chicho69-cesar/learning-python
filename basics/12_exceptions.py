### Exception Handling ###

numberOne = 5
numberTwo = 2
numberTwo = "2"

# Excepción base: try except
try:
    print(numberOne + numberTwo)
    print("No se ha producido ninguna excepción")
except TypeError:
    # Se ejecuta si se produce una excepción
    print("Se ha producido una excepción")

print("\n")

# Flujo completo de una excepción: try except else finally
try:
    print(numberOne + numberTwo)
    print("No se ha producido ninguna excepción")
except TypeError:
    print("Se ha producido una excepción")
else: # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continua exitosamente")
finally: # Opcional
    # Se ejecuta siempre
    print("La ejecución continua")

print("\n")

# Excepciones por tipo
try:
    print(numberOne + numberTwo)
    print("No se ha producido ninguna excepción")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

print("\n")

# Captura de la información de la excepción
try:
    print(numberOne + numberTwo)
    print("No se ha producido ninguna excepción")
except ValueError as error:
    print("ValueError")
    print(error)
except Exception as random_exc:
    print("Exception")
    print(random_exc)
