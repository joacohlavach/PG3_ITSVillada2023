class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print(f"Hola como andas {self.nombre}, como va tu día")

Persona1 = Persona(input("¿Cómo te llamas?: "))
Persona1.mostrar()