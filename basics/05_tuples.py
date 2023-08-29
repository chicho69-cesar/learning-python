### Tuples ###

# Definición
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (21, 1.79, "Cesar", "Villalobos Olmos", False, "Cesar")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(my_other_tuple)

# Acceso a elementos y búsqueda
print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[6]) # IndexError: tuple index out of range
# print(my_tuple[-7]) # IndexError: tuple index out of range

print(my_tuple.count("Cesar"))
print(my_tuple.index("Cesar"))
print(my_tuple.index("Villalobos Olmos"))

# my_tuple[1] = 1.80 # TypeError: 'tuple' object does not support item assignment

print("\n")

# Concatenación
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print("\n")

# Sub tuples
print(my_sum_tuple[3:6])
print("\n")

# Tupla mutable con conversión a lista
print(type(my_tuple))
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[5] = "Chicho"
my_tuple.insert(1, "Negro")

my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

print("\n")

# Eliminación
# del my_tuple[2] # TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) # NameError: name 'my_tuple' is not defined
