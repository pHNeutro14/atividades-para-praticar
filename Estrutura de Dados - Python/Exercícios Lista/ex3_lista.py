# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

texto = "abcdefghij"
cont_con = 0
vogais = "aeiou"

for letra in texto:
    if letra not in vogais:
        print(letra)
        cont_con += 1

print("Quantidade de consoantes:", cont_con)
