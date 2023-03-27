caracter = input("Ingrese el caracter que desea utilizar en el dibujo: ")
ancho = int(input("Ingrese el ancho del rectángulo: "))
alto = int(input("Ingrese el alto del rectángulo: "))

for i in range(alto):
    for j in range(ancho):
        print(caracter, end="")
    print()