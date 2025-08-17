# 1. Introducción a las Clases en Python
# Las clases son plantillas para crear objetos. Un objeto es una instancia de una clase.
# Nos permite agrupar datos (atributos o propiedades) y funciones (métodos) en un solo lugar.

OPENAI_KEY = ""
DEEPSEEK_API_KEY = ""

# Ejemplo básico de una clase
class Coche:
    # atributo de clase (comparte todas las instancias)
    tipo = "vehículo de cuatro ruedas"
    ruedas = 4

    # método especial que es el que construye el objeto
    # se llama automáticamente este método cuando creas la instancia
    def __init__(self, marca, modelo, color):
        # atributos de la instancia
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def arrancar(self):
        print(f"El coche {self.marca} {self.modelo} arrancó! 🚗")


mi_coche = Coche("Toyota", "Corolla", "rojo")
mi_coche.arrancar()

print(mi_coche.marca)

coche_de_pheralb = Coche("Ford", "Fiesta", "azul")
coche_de_pheralb.arrancar()

print(coche_de_pheralb.marca)

# Encapsulación: es ocultar los detalles internos de una clase y exponer solo la interfaz pública

# Crear una clase para llamar a la AI de OpenAI, DeepSeek O LO QUE SEA

import requests

class AI_API:
    def __init__(self, api_key, url, model):
        self.api_key = api_key
        self.url = url
        self.model = model

    def call(self, prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}]
        }

        try:
            response = requests.post(self.url, json=data, headers=headers)
            res_json = response.json()
            print(res_json["choices"][0]["message"]["content"])
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
            return None

print("\nOPEN_AI:")
openai_api = AI_API(OPENAI_KEY, "https://api.openai.com/v1/chat/completions", "gpt-4o-mini")

openai_api.call("Escribe un breve poema sobre la programación")

print("\nDEEPSEEK:")
deepseek_api = AI_API(DEEPSEEK_API_KEY, "https://api.deepseek.com/chat/completions", "deepseek-chat")

deepseek_api.call("Escribe un breve poema sobre la programación")



# Herencia, Abstracción, Polimorfismo y Encapsulación
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)  # Llama al constructor de la clase base
        self.curso = curso

    def presentarse(self):
        super().presentarse()  # Llama al método de la clase base
        print(f"Estoy estudiando {self.curso}.")

class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    def presentarse(self):
        super().presentarse()
        print(f"Enseño {self.asignatura}.")

class Universitario(Estudiante, Profesor):
    def __init__(self, nombre, edad, curso, asignatura):
        Estudiante.__init__(self, nombre, edad, curso)
        Profesor.__init__(self, nombre, edad, asignatura)

    def presentarse(self):
        Estudiante.presentarse(self)
        print(f"También enseño {self.asignatura}.")

universitario = Universitario("Ana", 22, "Ingeniería", "Matemáticas")
universitario.presentarse()
