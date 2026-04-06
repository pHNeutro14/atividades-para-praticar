"""Faça um Programa que peça as quatro notas de 3 alunos, calcule e
armazene num vetor a média de cada aluno, imprima o número de alunos
com média maior ou igual a 6.0."""

medias = []
alunos_aprovados = 0

for i in range(3):
    soma_notas = 0

    for j in range(4):
        nota = float(input(f"Insira a {j}° nota do {i}° aluno: "))
        soma_notas += nota

    media = soma_notas / 4
    medias.append(media)

    if media >= 6.0:
        alunos_aprovados += 1

print("Médias dos alunos:", medias)
print(f"Número de alunos com média >= 6.0: {alunos_aprovados}")
