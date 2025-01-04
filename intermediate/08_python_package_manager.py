### Python Package Manager ###
# PIP https://pypi.org

# pip install pip
# pip --version

# pip install numpy
# pip install pandas

# pip list
# pip unistall pandas
# pip show numpy


import pandas
import requests
import numpy
import matplotlib
import seaborn
from mypackage import arithmetics

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))

print(numpy_array * 2)

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

# Arithmetics package

print(arithmetics.suma(10, 2))
print(arithmetics.resta(10, 2))
print(arithmetics.mult(10, 2))
print(arithmetics.div(10, 2))
print(arithmetics.pot(10, 2))
print(arithmetics.raiz(100, 2))
print(arithmetics.log(100, 10))
print(arithmetics.mod(11, 2))
