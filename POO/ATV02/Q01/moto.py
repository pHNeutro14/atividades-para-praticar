class Moto:
    def __init__(self, marca, modelo, cilindradas):
        self.marca = marca
        self.modelo = modelo
        self.cilindradas = cilindradas

    def dados(self):
        return f"A moto {self.modelo} possui {self.cilindradas} cilindradas"
