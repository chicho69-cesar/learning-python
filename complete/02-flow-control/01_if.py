###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

from os import system

if system("clear") != 0:
    system("cls")

print("\n Sentencia simple condicional")
# Podemos usar la palabra clave "if" para ejecutar un bloque de código
# solo si se cumple una condición.
age = 18
if age >= 18:
    print("Eres mayor de edad")
    print("¡Felicidades!")

# Si no se cumple la condición, no se ejecuta el bloque de código
age = 15
if age >= 18:
    print("Eres mayor de edad")
    print("¡Felicidades!")

# Podemos usar el comando "else" para ejecutar un bloque de código
# si no se cumple la condición anterior del if
print("\n Sentencia condicional con else")
age = 15
if age >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("\n Sentencia condicional con elif")
grade = 5

# Además de usar "if" y "else", podemos usar "elif" para determinar
# múltiples condiciones, ten en cuenta que sólo se ejecutará el primer bloque
# de código que cumpla la condición (o la del else, si está presente)
if grade >= 9:
    print("¡Sobresaliente!")
elif grade >= 7:
    print("Notable!")
elif grade >= 5:
    print("¡Aprobado!")
else:
    print("¡No está calificado!")

print("\n Condiciones múltiples")
age = 16
has_permission = True

# Los operadores lógicos en Python son:
# and: True si ambos operandos son verdaderos
# or: True si al menos uno de los operandos es verdadero
# En JavaScript:
# && sería and
# || sería or

# En el caso que seas mayor de edad y tengas carnet...
# entonces podrás conducir
if age >= 18 and has_permission:
    print("Puedes conducir 🚗")
else:
    print("POLICIA 🚔!!!1!!!")

# En un pueblo de Isla Margarita son más laxos y
# te dejan conducir si eres mayor de edad O tienes carnet
if age >= 18 or has_permission:
    print("Puedes conducir en la Isla Margarita 🚗")
else:
    print("Paga al policía y te deja conducir!!!")

# También tenemos el operador lógico "not"
# que nos permite negar una condición
it_is_weekend = False
# JavaScript -> !
if not it_is_weekend:
    print("Cesar, venga que hay que streamear!")

# Podemos anidar condicionales, uno dentro del otro
# para determinar múltiples condiciones aunque
# siempre intentaremos evitar esto para simplificar
print("\n Anidar condicionales")
age = 20
has_money = True

if age >= 18:
    if has_money:
        print("Puedes ir a la discoteca")
    else:
        print("Quédate en casa")
else:
    print("No puedes entrar a la disco")

# Más fácil sería:
# if age < 18:
#   print("No puedes entrar a la disco")
# elif has_money:
#   print("Puedes ir a la discoteca")
# else:
#   print("Quédate en casa")

# Ten en cuenta que hay valores que al usarlos como condiciones
# en Python son evaluados como verdaderos o falsos
# por ejemplo, el número 5, es True
number = 5
if number: # True
    print("El número no es cero")

# Pero el número 0 se evalúa como False
number = 0
if number: # False
    print("Aquí no entrará nunca")

# También el valor vacío "" se evalúa como False
nombre = ""
if nombre:
    print("El nombre no es vacío")

# ¡Ten cuidado con no confundir la asignación = con la comparación ==!
number = 3 # asignación
is_number_three = number == 3 # comparación

if is_number_three:
    print("El número es 3")

# A veces podemos crear condicionales en una sola línea usando
# las ternarias, es una forma concisa de un if-else en una línea de código
print("\nLa condición ternaria:")
# [código si cumple la condición] if [condicion] else [codigo si no cumple]

age = 17
message = "Es mayor de edad" if age >= 18 else "Es menor de edad"
print(message)

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
print("\nEjercicio 1:")
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print("Los números son iguales")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
print("\nEjercicio 2:")
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operation = input("Introduce la operación (+, -, *, /): ")

result = None

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Error: No se puede dividir por cero.")
    else:
        result = num1 / num2
else:
    print("Operación no válida.")

print(f"El resultado es: {result}")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
print("\nEjercicio 3:")
year = int(input("Introduce un año: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} es un año bisiesto.")
else:
    print(f"{year} no es un año bisiesto.")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)
print("\nEjercicio 4:")
age = int(input("Introduce una edad: "))

if 0 <= age <= 2:
    print("Bebé")
elif 3 <= age <= 12:
    print("Niño")
elif 13 <= age <= 17:
    print("Adolescente")
elif 18 <= age <= 64:
    print("Adulto")
elif age >= 65:
    print("Adulto mayor")
else:
    print("Edad no válida.")
