###
# 02 - Bucles (for)
# Permiten ejecutar un bloque de código repetidamente mientras ITERA un iterable o una lista
###

from os import system

if system("clear") != 0:
    system("cls")

print("\nBucle for:")

# Iterar una lista
fruits = ["manzana", "pera", "mandarina"]
for fruit in fruits:
    print(fruit)

# Iterar sobre cualquier cosa que sea iterable
string = "midudev"
for char in string:
    print(char)

# enumerate()
fruits = ["manzana", "pera", "mandarina"]
for idx, value in enumerate(fruits):
    print(f"El índice es {idx} y la fruta es {value}")

# bucles anidados
letters = ["A", "B", "C"]
numbers = [1, 2, 3]

for letter in letters:
    for number in numbers:
        print(f"{letter}{number}")


# break
print("\nbreak:")
animals = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animals):
    print(animal)
    if animal == "loro":
        print(f"El loro está escondido en el índice {idx}")
        break

# continue
print("\ncontinue:")
animals = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animals):
    if animal == "loro":
        continue
    print(animal)

# Comprensión de listas (list comprehension)
animals = ["perro", "gato", "raton", "loro", "pez", "canario"]
animales_uppers = [animal.upper() for animal in animals]
print(animales_uppers)

# Muestra los números pares de una lista
pairs = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(pairs)

###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")

for num in range(2, 21, 2):
    print(num)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")
numbers = [10, 20, 30, 40, 50]
sum = 0

for number in numbers:
    sum += number

media = sum / len(numbers)
print(f"La media es: {media}")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")
numbers = [15, 5, 25, 10, 20]
max = numbers[0]

for number in numbers:
    # if number > max:
    #     max = number

    max = number if number > max else max

print(f"El número máximo es: {max}")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")
words = ["casa", "arbol", "sol", "elefante", "luna"]
long_words = [palabra for palabra in words if len(palabra) > 5]
print(f"Palabras con más de 5 letras: {long_words}")

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")
words = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
result = []
letter = input("Introduce una letra: ").lower()
counter = 0

for palabra in words:
    if palabra.lower().startswith(letter):
        counter += 1
        result.append(palabra)

print(f"Hay {counter} palabras que empiezan con la letra '{letter}'.")
print(f"Palabras que empiezan con '{letter}': {result}")
