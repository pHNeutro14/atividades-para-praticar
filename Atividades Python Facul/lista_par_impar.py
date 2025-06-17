lista = [8, 167, 12897, 892]
lista_par = []
lista_impar = []

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        print(f"> O número na posição {i} = {lista[i]} é par")
        lista_par.append(lista[i])
    else:
        print(f"> O número na posição {i} = {lista[i]} é impar")
        lista_impar.append(lista[i])

print(f"> Lista de números pares: {lista_par}")
print(f"> Lista de números impares: {lista_impar}")