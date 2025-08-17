### Functions ###

# Definición
def my_function():
    print("Hello from a function")

my_function()
my_function()
my_function()

print("\n")

# Función con parámetros de entrada/argumentos
def sum_func(first: int, second):
    print(first + second)

sum_func(5, 7)
sum_func(54754, 71231)
sum_func("5", "7")
sum_func(1.4, 5.2)

print("\n")

# Función con parámetros de entrada/argumentos y retorno
def sum_with_return(first: int, second: int) -> int:
    my_sum = first + second
    return my_sum

my_result = sum_with_return(1.4, 5.2)
print(my_result)

my_result = sum_with_return(10, 5)
print(my_result)

print("\n")

# Función con parámetros de entrada/argumentos por clave
def print_info(name, lastname):
    print(f"{name} {lastname}")

print_info(name="Cesar", lastname="Villalobos Olmos")
print("\n")

# Función con parámetros de entrada/argumentos por defecto
def print_user(name, lastname, nick="nick"):
    print(f"{name} {lastname} {nick}")

print_user("Cesar", "Villalobos Olmos")
print_user("Liz", "Sandoval Vallejo", "Chamita")
print("\n")

# Función con parámetros de entrada/argumentos arbitrarios
def print_upper_texts(*texts):
    print(type(texts))

    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Mundo", "With", "Python")
print_upper_texts("Hola")
