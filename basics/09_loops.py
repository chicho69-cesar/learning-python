### Loops ###

# While
my_counter = 0

while my_counter < 10:
    print(my_counter)
    my_counter += 2
else: # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continua\n")

while my_counter <= 20:
    my_counter += 1

    if my_counter == 15:
        print("Se detiene la ejecución")
        break

    print(my_counter)

print("La ejecución continua\n")

# For

print("\n")
my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

print("\n")
my_tuple = (21, 1.79, "Cesar", "Villalobos Olmos", True)

for element in my_tuple:
    print(element)

print("\n")
my_set = { "Cesar", "Chicho", "cesar-09@hotmail.com" }

for element in my_set:
    print(element)

print("\n")
my_dict = {
    "Name": "Cesar",
    "Lastname": "Villalobos Olmos",
    "Age": 21,
    1: "Python"
}

for key, value in my_dict.items():
    print(key) # Result: 'Name', 'Lastname', 'Age', 1
    print(value) # Result: 'Cesar', 'Villalobos Olmos', 21, 'Python'
else:
    print("El bucle for ha finalizado")

print("\nLa ejecución continúa\n")

for element in my_dict:
    print(element)

    if element == "Age":
        break # No se ejecuta el else
else:
    print("El bucle for ha finalizado")

print("\nLa ejecución continúa\n")

for element in my_dict:
    print(element)

    if element == "Age":
        continue

    print("Se ejecuta")
else:
    print("El bucle for ha finalizado")

print("\n")

for i in range(11):
    print(i)

print("\n")

for i in range(1, 11):
    print(i)

print("\n")

for i in range(1, 11, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)
