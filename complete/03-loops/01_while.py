###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
###

from os import system

if system("clear") != 0:
    system("cls")

print("\n Bucle while:")

# Bucle con una simple condición
counter = 0

while counter <= 5:
    print(counter)
    counter += 1 # es super importante para evitar un bucle infinito

# utilizando la palabra break, para romper el bucle
print("\n Bucle while con break:")
counter = 0

while True:
    print(counter)
    counter += 1
    if counter == 5:
        break # sale del bucle

# continue, que lo hace es saltar esa iteración en concreto
# y continuar con el bucle
print("\n Bucle con continue")
counter = 0
while counter < 10:
    counter += 1

    if counter % 2 == 0:
        continue

    print(counter)

# else, esta condición cuando se ejecuta?
print("\n Bucle while con else:")
counter = 0
while counter < 5:
    print(counter)
    counter += 1
else:
    print("El bucle ha terminado")

# else, esta condición cuando se ejecuta?
print("\n Bucle while con else:")
counter = 0
while counter < 5:
    print(counter)
    counter += 1
else:
    print("El bucle ha terminado")

# pedirle al usuario un número que tiene
# que ser positivo si no, no le dejamos en paz
number = -1
while number < 0:
    number = int(input("Escribe un número positivo: "))
    if number < 0:
        print("El número debe ser positivo. Intenta otra vez, majo o maja.")

print(f"El número que has introducido es {number}")

number = -1
while number < 0:
    try:
        number = int(input("Escribe un número positivo: "))
        if number < 0:
            print("El número debe ser positivo. Intenta otra vez, majo o maja.")
    except:
        print("Lo que introduces debe ser un número, que si no peta!")

print(f"El número que has introducido es {number}")

###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")
counter = 10
while counter > 0:
    print(counter)
    counter -= 1  # Decrementa el contador en 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")
sum = 0
number = 1

while number <= 20:
    if number % 2 == 0:  # Verifica si el número es par
        sum += number
    number += 1  # Incrementa el número en 1

print(f"La suma de los números pares entre 1 y 20 es: {sum}")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")
number = int(input("Introduce un número entero positivo para calcular su factorial: "))
factorial = 1
counter = 1

while counter <= number:
    factorial *= counter  # Multiplica el factorial por el contador actual
    counter += 1  # Incrementa el contador en 1

print(f"El factorial de {number} es: {factorial}")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")
password = input("Introduce una contraseña (debe tener al menos 8 caracteres): ")
while len(password) < 8:
    print("Contraseña inválida. Debe tener al menos 8 caracteres.")
    password = input("Introduce una contraseña (debe tener al menos 8 caracteres): ")

print("Contraseña válida.")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")
number = int(input("Introduce un número para ver su tabla de multiplicar: "))
counter = 1

while counter <= 10:
    resultado = number * counter
    print(f"{number} x {counter} = {resultado}")
    counter += 1  # Incrementa el contador en 1

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")
number = int(input("Introduce un número entero positivo N para encontrar números primos: "))
counter = 2  # Comenzamos desde el primer número primo

while counter <= number:
    is_prime = True  # Asumimos que el número es primo
    divisor = 2

    # while divisor <= contador // 2:
    #     if contador % divisor == 0:  # Si es divisible por otro número, no es primo
    #         es_primo = False
    #         break
    #     divisor += 1

    while divisor * divisor <= counter:  # Optimización: solo verificar hasta la raíz cuadrada
        if counter % divisor == 0:  # Si es divisible por otro número, no
            is_prime = False
            break
        divisor += 1

    if is_prime:
        print(counter)  # Imprime el número primo encontrado

    counter += 1  # Incrementa el contador en 1
