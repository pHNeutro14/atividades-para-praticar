matriz = [
    [8, 9, 3],
    [7, 2, 45],
    [1, 20, 31]
]

i = 0

while i < len(matriz):
    j = 0

    while j < len(matriz[0]):
        print(f"Linha: {i+1} Coluna {j+1} = {matriz[i][j]}", end='\t')
        j = j + 1

    print(" ")
    
    i = i + 1