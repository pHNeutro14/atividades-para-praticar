def particao(lista, l, r):
    pivo = lista[l]
    i = l - 1
    j = r + 1

    while True:
        # mylist = [64, 34, 25, 5, 22, 11, 90, 12]
        # move i para a direita
        i += 1
        while lista[i] < pivo:
            i += 1

        # move j para a esquerda
        j -= 1
        while lista[j] > pivo:
            j -= 1

        if i >= j:
            return j

        lista[i], lista[j] = lista[j], lista[i]


def quicksort(lista, l=0, r=None):
    if r is None:
        r = len(lista) - 1

    if l < r:
        p = particao(lista, l, r)
        quicksort(lista, l, p)
        quicksort(lista, p + 1, r)


mylist = [64, 34, 25, 5, 22, 11, 90, 12]
quicksort(mylist)
print(mylist)
