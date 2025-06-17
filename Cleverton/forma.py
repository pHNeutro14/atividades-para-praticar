class Forma:
    def calcular_area(self): pass

class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return f"Retângulo: {self.base * self.altura}cm"

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return f"{3.14 * (self.raio ** 2)}"

ret1 = Retangulo(4, 5)
print(ret1.calcular_area())
circ1 = Circulo(4)
print(circ1.calcular_area())