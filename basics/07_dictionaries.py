### Dictionaries ###

# Definición
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {
    "Name": "Cesar",
    "Lastname": "Villalobos Olmos",
    "Age": 21,
    1: "Python"
}

my_dict = {
    "Name": "Cesar",
    "Lastname": "Villalobos Olmos",
    "Age": 21,
    "Languages": ["Python", "Java", "C#"],
    1: 1.79
}

print(my_dict)
print(my_other_dict)

print(len(my_dict))
print(len(my_other_dict))

print("\n")

# Búsqueda
print(my_dict[1])
print(my_dict["Name"])

print("Cesar" in my_dict)
print("Lastname" in my_dict) # Key in dict

print("\n")

# Inserción
my_dict["Street"] = "Av Canal #9"
print(my_dict)
print("\n")

# Actualización
my_dict["Languages"] = ["Python", "C#", "JavaScript", "TypeScript"]
print(my_dict)
print("\n")

# Eliminación
del my_dict["Street"]
print(my_dict)
print("\n")

# Otras operaciones
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

print(type(my_dict.items()))
print(type(my_dict.keys()))
print(type(my_dict.values()))

print("\n")

my_list = ["Name", 1, "Lang"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys(("Name", 1, "Lang"))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, "Chicho") # Valor por defecto para cada key
print(my_new_dict)

print("\n")

my_values = my_new_dict.values()
print(my_values)
print(type(my_values))

print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))
