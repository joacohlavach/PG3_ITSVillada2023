def suma():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = num1 + num2
            print("El resultado es: ", resultado)
            resultado = input("¿Desea seguir sumando valores? (s/n): ")
            if resultado.lower() != "s":
                break
        except ValueError:
            print("Error, solo se pueden ingresar números enteros")
        
suma()