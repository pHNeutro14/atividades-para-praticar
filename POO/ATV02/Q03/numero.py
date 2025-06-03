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

