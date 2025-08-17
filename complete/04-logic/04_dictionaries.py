###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados.
###

from os import system
if system("clear") != 0:
    system("cls")

# ejemplo tipico de diccionario
person = {
  "nombre": "midudev",
  "edad": 25,
  "es_estudiante": True,
  "calificaciones": [7, 8, 9],
  "socials": {
    "twitter": "@midudev",
    "instagram": "@midudev",
    "facebook": "midudev"
  }
}

# para acceder a los valores
print(person["nombre"])
print(person["calificaciones"][2])
print(person["socials"]["twitter"])

# cambiar valores al acceder
person["nombre"] = "madeval"
person["calificaciones"][2] = 10

# eliminar completamente una propiedad
del person["edad"]
# print(persona)

is_student = person.pop("es_estudiante")
print(f"es_estudiante: {is_student}")
print(person)

# sobre escribir un diccionario con otro diccionario
a = { "name": "miduev", "age": 25 }
b = { "name": "madeval", "es_estudiante": True }

a.update(b)
print(a)

# comprobar si existe una propiedad
print("name" in person) # False
print("nombre" in person) # True

# obtener todas las claves
print("\nkeys:")
print(person.keys())

# obtener todas los valores
print("\nvalues:")
print(person.values())

# obtener tanto clave como valor
print("\nitems:")
print(person.items())

for key, value in person.items():
    print(f"{key}: {value}")
