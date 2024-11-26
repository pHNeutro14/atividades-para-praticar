a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = (b**2 - 4 * a * c)
print(f"Valor de delta: {delta}")

if delta < 0:
    print("Não possui raiz real!!")

else:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print(f"x1 = {x1} x2 = {x2}")

    if delta == 0:
        print(f"O valor de x1 é igual a x2")
