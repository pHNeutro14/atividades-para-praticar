"""Faça um programa que leia 15 números inteiros e armazene-os num
vetor. Armazene os números pares no vetor PAR e os números IMPARES
no vetor impar. Imprima os três vetores."""

i = 1
numeros = []
par = []
impar = []
while i <= 15:
    num = int(input(f"Insira o {i}° número: "))
    numeros.append(num)

    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

    i = i + 1

print(f"Lista de Números: {numeros}")
print(f"Lista de Números pares: {par}")
print(f"Lista de Números Ímpares: {impar}")
