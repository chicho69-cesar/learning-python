### Sets ###

# Definición
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = { "Cesar", "Villalobos Olmos", 21 }
print(type(my_other_set))
print(len(my_other_set))

print("\n")

# Inserción
my_other_set.add("Chicho")
print(my_other_set) # Los sets no tienen orden

my_other_set.add("Negro")
print(my_other_set)

print("\n")

# Búsqueda
print("Chicho" in my_other_set)
print("Chiche" in my_other_set)

print("\n")

# Eliminación
my_other_set.remove("Negro")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set) # NameError: name 'my_other_set' is not defined

print("\n")

# Transformación
my_set = { "Cesar", "Villalobos Olmos", 21 }
my_list = list(my_set)

print(my_list)
print(my_list[0])

my_other_set = { "JavaScript", "TypeScript", "Python", "Php", "C#", "Java", "Dart" }
print(my_other_set)

print("\n")

# Otras operaciones
my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union(my_new_set).union(my_set).union({ "Go", "Rust" }))
print(my_new_set.difference(my_set))
