###
# 03 - Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
###

from os import system
if system("clear") != 0: system("cls")

# Creación de listas
print("\nCrear listas")
list1 = [1, 2, 3, 4, 5] # lista de enteros
list2 = ["manzanas", "peras", "plátanos"] # lista de cadenas
list3 = [1, "hola", 3.14, True] # lista de tipos mixtos

empty_list = []
list_of_lists = [[1, 2], ['calcetin', 4]]
matrix = [[1, 2], [2, 3], [4, 5]]

print(list1)
print(list2)
print(list3)
print(empty_list)
print(list_of_lists)
print(matrix)

# Acceso a elementos por índice
print("\nAcceso a elementos por índice")
print(list2[0])  # manzanas
print(list2[1])  # peras
print(list2[-1]) # plátanos
print(list2[-2]) # peras

print(list_of_lists[1][0])

# Slicing (rebanado) de listas
list1 = [1, 2, 3, 4, 5]
print(list1[1:4]) # [2, 3, 4]
print(list1[:3]) # [1, 2, 3]
print(list1[3:]) # [4, 5]
print(list1[:]) # [1, 2, 3, 4, 5]

# El tercer parámetro es el paso (step)
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(list1[::2]) # para devolver índices pares
print(list1[::-1]) # para devolver índices inversos

# Modificar una lista
list1[0] = 20
print(list1)

# Añadir elementos a una lista
list1 = [1, 2, 3]

# forma larga y menos eficiente
list1 = list1 + [4, 5, 6]
print(list1)

# forma corta y más eficiente
list1 += [7, 8, 9]
print(list1)

# Recuperar longitud de una lista
print("Longitud de la lista", len(list1))

###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
message = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
code = message[7:14]
print("Mensaje: {}".format("".join(code)))

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.
numbers = [10, 20, 30, 40, 50]
numbers[0], numbers[-1] = numbers[-1], numbers[0]

print("Lista después del intercambio:", numbers)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
sandwich = pan + ingredientes + pan_abajo
print("Sándwich:", sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
list = [1, 2, 3]
duplicated = list * 2 # Opción 1: Usando el operador de repetición
duplicated = list + list # Opción 2: Usando concatenación
print("Lista duplicada:", duplicated)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30
list = [10, 20, 30, 40, 50]
center = list[len(list) // 2:len(list) // 2 + 1][0]  # Opción 1: Usando el índice del centro
print("Elemento del centro:", center)

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
list = [1, 2, 3, 4, 5, 6]
half = len(list) // 2
reverse_partial = list[:half][::-1] + list[half:]
print("Reversa parcial:", reverse_partial)
