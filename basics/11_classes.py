### Classes ###

# Definición
class MyEmptyClass:
    pass # Para poder dejar la clase vacía

print(MyEmptyClass)
print(MyEmptyClass())

# Clase con constructor, funciones y propiedades privadas y públicas
class Person:
    def __init__(self, name, lastname, nick="Sin nick"):
        self.full_name = f"{name} {lastname} ({nick})" # Propiedad pública
        self.__have_nick = nick != "Sin nick" # Propiedad privada

        self.name = name
        self.lastname = lastname
        self.nick = nick

    def get_name(self):
        return self.name
    
    def walk(self):
        print(f"{self.full_name} está caminando")

    def get_have_nick(self):
        return self.__have_nick

print("\n")

my_person = Person("Cesar", "Villalobos Olmos")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

print("\n")

my_other_person = Person("Cesar", "Villalobos Olmos", "Chicho")
print(my_other_person.full_name)
my_other_person.walk()

print("\n")

my_other_person.full_name = "Cesar Villalobos Olmos (Dev)"
print(my_other_person.full_name)

print("\n")

my_other_person.full_name = 123
print(my_other_person.full_name)
