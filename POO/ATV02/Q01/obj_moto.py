import moto

moto1 = moto.Moto("Honda", "Honda CB 500F", 500)
moto2 = moto.Moto("Yamaha", "Yamaha YZF-R6", 600)

print(moto1.dados())
print(moto2.dados())