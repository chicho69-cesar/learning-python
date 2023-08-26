### Variables ###

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones útiles
print(len(my_string_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, lastname, age, nick = "Cesar", "Villalobos Olmos", 21, "chicho"
print("Me llamo:", name, lastname, "tengo", age, "años y mi apodo es", nick)

# Inputs
name = input("¿Cuál es tu nombre?: ")
age = input("¿Cuál es tu edad?: ")

print(name)
print(age)

# Cambiamos su tipo
name = 21
age = "Cesar"

print(name)
print(age)

# Forzamos el tipo
address: str = "Calle falsa 123"
address = True
address = 5
address = 1.2

# A pesar de que podemos especificar el tipo de variable, python lo reconoce dinamicamente
print(type(address))
