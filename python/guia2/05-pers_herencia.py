class Persona:
    def __init__(self ,nom, ape):
        self.nombre = nom
        self.apellido = ape



class Empleado(Persona):
    def __init__(self, nom, ape):
        super().__init__(nom, ape)

    def sueldo(self, suel):
        self.suel = suel
        if self.suel >= 3000:
            print("Tiene que pagar impuestos pagar impuestos")
        else:
            print("No tiene que pagar impuestos")


nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
sueldo = int(input("Ingresa tu sueldo: "))

em =Empleado(nombre, apellido)
em.sueldo(sueldo)