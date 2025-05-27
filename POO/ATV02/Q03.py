class Numero:
    def __init__(self, num):
        self.num = num

    def sucessor(self):
        valor = self.num + 1
        print(f'O sucessor de {self.num} é {valor}')

    def antecessor(self):
        valor = self.num - 1
        print(f'O antecessor de {self.num} é {valor}')

    def dobro(self):
        valor = self.num * 1
        print(f'O dobro de {self.num} é {valor}')

    def triplo(self):
        valor = self.num * 3
        print(f'O triplo de {self.num} é {valor}')  

    def metade(self):
        valor = self.num / 2
        print(f'A metade de {self.num} é {valor}')    

num1 = Numero(2)
num2 = Numero(8)
num1.sucessor()
num2.sucessor()
num1.antecessor()
num2.antecessor()
num1.dobro()
num2.dobro()
num1.triplo()
num2.triplo()
num1.metade()
num2.metade()
