# Declarar um array (lista) unidimensional
array1 = [0] * 5

# Declarar e definir valores do array
array2 = [1, 3, 5, 7, 9]

# Sintaxe alternativa
array3 = [1, 2, 3, 4, 5, 6]

# Declarar um array bidimensional (matriz 2x3)
multiDimensionalArray1 = [[0 for _ in range(3)] for _ in range(2)]

# Declarar e definir valores do array
multiDimensionalArray2 = [[1, 2, 3], [4, 5, 6]]

# Declarar um array irregular (jagged array)
jaggedArray = [None] * 6

# Definir os valores do primeiro array dentro da estrutura jagged
jaggedArray[0] = [1, 2, 3, 4]

print("array1:", array1)
print("array2:", array2)
print("array3:", array3)
print("multiDimensionalArray1:", multiDimensionalArray1)
print("multiDimensionalArray2:", multiDimensionalArray2)
print("jaggedArray:", jaggedArray)
