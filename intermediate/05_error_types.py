### Error Types ###

# SyntaxError
# print "¡Hola comunidad!" # Des comentar para Error
from math import pi
import math
print("¡Hola python!")

# NameError
language = "Spanish"  # Comentar para Error
print(language)

# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
# print(my_list[5]) # Des comentar para Error

# ModuleNotFoundError
# import maths # Des comentar para Error

# AttributeError
# print(math.PI) # Des comentar para Error
print(math.pi)

# KeyError
my_dict = {"Nombre": "Cesar", "Apellido": "Villalobos Olmos", "Edad": 22, 1: "Python"}
print(my_dict["Edad"])
# print(my_dict["Apelido"]) # Des comentar para Error
print(my_dict["Apellido"])

# TypeError
# print(my_list["0"]) # Des comentar para Error
print(my_list[0])
print(my_list[False])

# ImportError
# from math import PI # Des comentar para Error
print(pi)

# ValueError
#my_int = int("10 Años")
my_int = int("10")  # Des comentar para Error
print(type(my_int))

# ZeroDivisionError
# print(4/0) # Des comentar para Error
print(4/2)
