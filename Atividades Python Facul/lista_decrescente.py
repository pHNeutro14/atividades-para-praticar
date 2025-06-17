lista = [12,11,15,4,6,7,1,2]

i = 0

while i < len(lista) - 1:
    if lista[i] < lista[i+1]:
        a = lista[i]
        b = lista[i + 1]
        c = a
        lista[i] = b
        lista[i+1] = c

        if i > 0:
            i = i - 1
    else:
        i = i+ 1

print(lista)