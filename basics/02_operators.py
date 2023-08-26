### Operadores ###

#* Operadores aritméticos

# Operaciones con enteros
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3) # Division exacta
print(2 ** 3) # Potencia
print(2 ** 3 + 3 - 7 / 1 // 4)

# Operaciones con cadenas de texto
print("Hola " + "Python" + " ¿Que tal?")
print("Hola " + str(5))

# Operaciones mixtas
print("Hola " * 5) # Repite la cadena de texto 5 veces
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola", int(my_float))

#* Operadores Comparativos

# Operaciones con enteros
print(3 < 4)
print(3 > 4)
print(3 <= 4)
print(3 >= 4)
print(3 == 4)
print(3 != 4)

# Operaciones con cadenas de texto
print("Hola" < "Python")
print("Hola" > "Python")
print("Hola" <= "Python")
print("Hola" >= "Python")
print("Hola" == "Python")
print("Hola" != "Python")
print("Hola" == "Hola")
print("aaaa" >= "abaa") # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa")) # Cuenta caracteres

#* Operadores Lógicos

# Basada en el Álgebra de Boole
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" < "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not 3 < 4)
