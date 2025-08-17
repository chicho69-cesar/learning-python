###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0:
    system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

city, country = input("Escribe tu ciudad y país separados por coma: ").split(", ")
print(f"Hola, me llamo Cesar y vivo en {city}, {country}.")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print(f"Variable a: {a}, tipo: {type(a)}")
print(f"Variable b: {b}, tipo: {type(b)}")
print(f"Variable c: {c}, tipo: {type(c)}")
print(f"Variable d: {d}, tipo: {type(d)}")
print(f"Variable e: {e}, tipo: {type(e)}")

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

number = "12345"
number_int = int(number)
number_float = float(number_int)

print(f"Cadena original: {number}, convertido a entero: {number_int}, convertido a float: {number_float}")

float_number = 3.99
int_from_float = int(float_number)

print(f"Float original: {float_number}, convertido a entero: {int_from_float}")

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

name, age, height = "Cesar", 23, 1.79
print("Hola, me llamo {} y tengo {} años. Mido {} metros.".format(name, age, height))

### Completa aquí

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

import math

PI = math.pi
PI = round(PI)
print(f"El número PI redondeado es: {PI}")
result = PI // 2
print(f"El resultado de la división entera entre {PI} y 2 es: {result}")
