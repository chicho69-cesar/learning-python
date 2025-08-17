###
# 04 - Listas Métodos
# Los métodos más importantes para trabajar con listas
###

from os import system
if system("clear") != 0:
    system("cls")

# Creamos una lista con valores
list1 = ['a', 'b', 'c', 'd']

# Añadir o insertar elementos a la lista
list1.append('e') # Añade un elemento al final
print(list1)

list1.insert(1, '@') # Inserta un elemento en la posición que le indiquemos como primer argumento
print(list1)

list1.extend(['😃', '😍']) # Agrega elementos al final de la lista
print(list1)

# Eliminar elementos de la lista
list1.remove('@') # Eliminar la primera aparición de la cadena de texto @
print(list1)

last = list1.pop() # Eliminar el último elemento de la lista y además te lo devuelve
print(last)
print(list1)

list1.pop(1) # Eliminar el segundo elemento de la lista (es el índice 1)
print(list1)

# Eliminar por lo bestia un índice
del list1[-1]
print(list1)

list1.clear() # Eliminar todos los elementos de la lista
print(list1)

# Eliminar un rango de elementos
list1 = ['🐼', '🐨', '🐶', '😿', '🐹']
del list1[1:3] # eliminamos los elementos del índice 1 al 3 (no incluye el índice 3)
print(list1)

# Más métodos útiles
print('Ordenar listas modificando la original')
numbers = [3, 10, 2, 8, 99, 101]
numbers.sort()
print(numbers)

print('Ordenar listas creando una nueva lista')
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print("Ordenar una lista de cadenas de texto (todo minúscula)")
fruits = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_fruits = sorted(fruits)
print(sorted_fruits)

print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
fruits = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
fruits.sort(key=str.lower)
print(fruits)

# Más cositas útiles
animals = ['🐶', '🐼', '🐨', '🐶']
print(len(animals)) # Tamaño de la listas -> 4
print(animals.count('🐶')) # Cuantas veces aparece el elemento '🐶' -> 2
print('🐼' in animals) # Comprueba si hay un '🐼' en la lista -> True
print('🐹' in animals) # -> False

###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.
print("\nEjercicio 1:")
list = [1, 2, 3, 4, 5]
list.append(6)
list.insert(2, 10)
list[0] = 0
print(list)  # Output: [0, 2, 10, 3, 4, 5, 6]

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# list_a = [1, 2, 3]
# list_b = [4, 5, 6, 1, 2]
# Extiende list_a con list_b usando extend().
# Elimina la primera aparición del número 1 en list_a usando remove().
# Elimina el elemento en el índice 3 de list_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente list_b usando clear().
print("\nEjercicio 2:")
list_a = [1, 2, 3]
list_b = [4, 5, 6, 1, 2]
list_a.extend(list_b)
list_a.remove(1)
deleted_element = list_a.pop(3)
print(f"Elemento eliminado: {deleted_element}") #Output: Elemento eliminado: 5
list_b.clear()
print("Lista a:", list_a) #Output: Lista a: [2, 3, 4, 6, 1, 2]
print("Lista b:", list_b) #Output: Lista b: []

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.
print("\nEjercicio 3:")
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del list[2:5]
print(list)  # Output: [1, 2, 6, 7, 8, 9, 10]

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.
print("\nEjercicio 4:")
list = [5, 2, 8, 1, 9, 4, 2]
list.sort()
two_quantity = list.count(2)
has_number_seven = 7 in list
print(f"Lista ordenada: {list}") #Output: Lista ordenada: [1, 2, 2, 4, 5, 8, 9]
print(f"Cantidad de 2: {two_quantity}") #Output: Cantidad de 2: 2
print(f"¿Está el 7?: {has_number_seven}") #Output: ¿Está el 7?: False

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copy_1 usando slicing.
# Crea otra copia llamada copy_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copy_1, copy_2, referencia) y observa los cambios.
print("\nEjercicio 5:")
original = [1, 2, 3]
copy_1 = original[:]  # Usando slicing
copy_2 = original.copy()  # Usando copy()
reference = original  # Referencia a la lista original
reference[0] = 10
print(f"Original: {original}")       # Output: Original: [10, 2, 3]
print(f"Copia 1 (slicing): {copy_1}") # Output: Copia 1 (slicing): [1, 2, 3]
print(f"Copia 2 (copy()): {copy_2}") # Output: Copia 2 (copy()): [1, 2, 3]
print(f"Referencia: {reference}")     # Output: Referencia: [10, 2, 3]

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
print("\nEjercicio 6:")
strings = ["Manzana", "pera", "BANANA", "naranja"]
strings.sort(key=str.lower)
print(strings) # Output: ['BANANA', 'Manzana', 'naranja', 'pera']
