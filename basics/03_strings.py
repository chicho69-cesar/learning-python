### Strings ###

my_string = "My String"
my_other_string = 'My Other String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\n con salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un \"String\" \\n con escape\n"
print(my_scape_string)

# Formateo
name, lastname, age = "Cesar", "Villalobos Olmos", 21
print("Mi nombre es {} {} y tengo {} años".format(name, lastname, age))
print("Mi nombre es %s %s y tengo %d años" % (name, lastname, age))
print("Mi nombre es " + name + " " + lastname + " y tengo " + str(age) + " años")
print(f"Mi nombre es {name} {lastname} y tengo {age} años")

# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(b, "\n")

# División
language_slice = language[1:3]
print(language_slice) # Result: 'yt'

language_slice = language[1:]
print(language_slice) # Result: 'ython'

language_slice = language[-2]
print(language_slice) # Result: 'o'

language_slice = language[-2:]
print(language_slice) # Result: 'on'

language_slice = language[0:6:2]
print(language_slice) # Result: 'pto'

# Reverse
language_reverse = language[::-1]
print(language_reverse, "\n") # Result: 'nohtyp'

# Funciones del lenguaje
print(language.capitalize())
print(language.upper())
print(language.lower())
print(language.count("t"))
print(language.isnumeric())
print(language.lower().isupper())
print(language.startswith("py"))
print(language.endswith("on"))
print("1".isnumeric())
print("Py" == "py") # Es case sensitive
