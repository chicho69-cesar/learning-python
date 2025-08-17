### Lists ###

# Definición
my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [21, 1.79, "Cesar", False, ["Python", "JavaScript"]]

print(type(my_list))
print(type(my_other_list))
print('\n')

# Acceso a elementos y búsqueda
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])

print(my_list.count(30))

# print(my_other_list[5]) # IndexError: list index out of range
# print(my_other_list[-6]) # IndexError: list index out of range

print(my_other_list.index("Cesar"))

# Aquí estamos desempaquetando la lista
age, height, name, is_married, languages = my_other_list
print(name)

name, age, height, is_married, languages = my_other_list[2], my_other_list[0], my_other_list[1], my_other_list[3], my_other_list[4]
print(name)
print('\n')

# Concatenación
print(my_list + my_other_list)
# print(my_list - my_other_list) # TypeError: unsupported operand type(s) for -: 'list' and 'list'
print('\n')

# Creación, inserción, actualización y eliminación
my_other_list.append("Chicho") # Añade al final de la lista
print(my_other_list)

my_other_list.insert(1, "Negro") # Inserta en la posición 1
print(my_other_list)

my_other_list[1] = "Gris"
print(my_other_list)

my_other_list.remove("Gris") # Elimina el primer elemento que coincida
print(my_other_list)

my_list.remove(30) # Elimina el primer elemento que coincida
print(my_list)

my_list.pop() # Elimina el último elemento
print(my_list)

my_popped_element = my_list.pop(2) # Elimina el elemento en la posición 2
print(my_popped_element)
print(my_list)

del my_list[2] # Elimina el elemento en la posición 2
print(my_list)

print('\n')

# Operaciones con listas
my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print('\n')

# Sub listas
print(my_new_list[1:3]) # Result: [24, 30]
print('\n')

print(my_new_list[::-1]) # Result: [62, 52, 30, 24, 17, 35]
print('\n')

# Cambio de tipo
my_list = "Hello Python"
print(my_list)
print(type(my_list))
