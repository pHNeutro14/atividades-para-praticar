class Moto:
    def __init__(self, marca, modelo, cilindradas):
        self.marca = marca
        self.modelo = modelo
        self.cilindradas = cilindradas

    def dados(self):
        return f"A moto {self.modelo} possui {self.cilindradas} cilindradas"
        
moto1 = Moto("Honda", "Honda CB 500F", 500)
moto2 = Moto("Yamaha", "Yamaha YZF-R6", 600)

print(moto1.dados())
print(moto2.dados())