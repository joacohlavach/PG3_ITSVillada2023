class Triangulo:
    def _init_(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def mayor(self):
        var = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado más grande es: {var}")

    def equilatero(self):
        if self.lado1==self.lado2==self.lado3:
        	print(f"es un triángulo equilatero")
      
lado1 = float(input(f"Medida del lado 1: "))
lado2 = float(input(f"Medida del lado 2: "))
lado3 = float(input(f"Medida del lado 3: "))

triangulo = Triangulo(lado1, lado2, lado3)
triangulo.mayor()
triangulo.equilatero()