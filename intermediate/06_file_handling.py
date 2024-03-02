### File Handling ###

import xml
import csv
import json
import os


# .txt file

# Leer, escribir y sobrescribir si ya existe
txt_file = open("my_file.txt", "w+")
txt_file.write("Mi nombre es Cesar\nMi apellido es Villalobos Olmos\n22 años\nY mi lenguaje preferido es Python")

# print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())

for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque también me gusta JavaScript")
print(txt_file.readline())

txt_file.close()

with open("my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY TypeScript")

# os.remove("my_file.txt")


# .json file

json_file = open("my_file.json", "w+")

json_test = {
    "name": "Cesar",
    "surname": "Villalobos Olmos",
    "age": 22,
    "languages": ["Python", "JavaScript", "TypeScript"],
    "website": "https://github.com/chicho69-cesar"
}

json.dump(json_test, json_file, indent=2)

json_file.close()

with open("my_file.json", "r") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dic = json.load(open("my_file.json"))

print(json_dic)
print(type(json_dic))
print(json_dic["name"])


# .csv file

csv_file = open("my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Cesar", "Villalobos Olmos", 22, "Python", "https://github.com/chicho69-cesar"])
csv_writer.writerow(["Roswell", "", 2, "JavaScript", ""])

csv_file.close()

with open("my_file.csv", "r") as my_other_file:
    for line in my_other_file.readlines():
        print(line)


# .xlsx file
# import xlrd # Debe instalarse con pip install xlrd


# .xml file

xml_file = open("my_file.xml", "w+")

xml_file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
xml_file.write("<person>\n")
xml_file.write("\t<name>Cesar</name>\n")
xml_file.write("\t<surname>Villalobos Olmos</surname>\n")
xml_file.write("\t<age>22</age>\n")
xml_file.write("\t<languages>\n")
xml_file.write("\t\t<language>Python</language>\n")
xml_file.write("\t\t<language>JavaScript</language>\n")
xml_file.write("\t\t<language>TypeScript</language>\n")
xml_file.write("\t</languages>\n")
xml_file.write("\t<website>https://github.com/chicho69-cesar</website>\n")
xml_file.write("</person>")

xml_file.close()

with open("my_file.xml", "r") as my_other_file:
    for line in my_other_file.readlines():
        print(line)
