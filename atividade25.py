# Enunciado: Crie um programa que receba a nota de 5 alunos e exiba quantos foram aprovados (nota maior ou igual a 7).

alunos_aprovados=0

for n in range(1, 6):
    nota = float(input("digite a nota do aluno: "))
    if nota >=7:
        alunos_aprovados += 1

print(f"{alunos_aprovados} alunos foram aprovados ")

        

