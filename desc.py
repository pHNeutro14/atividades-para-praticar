num = float(input("Insira um valor para calcular o desconto: "))
desc = float(input("Insira o desconto: "))
calc_desc = num - (num * desc/100)

if calc_desc >= 100:
    print(f"O valor total pós desconto é igual a: {calc_desc}")

print("fim")
