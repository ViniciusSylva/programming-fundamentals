print("==SORTEIO PARA APAGAR O QUADRO==")

import random

aluno1 = input("Qual o nome do 1° aluno? ")
aluno2 = input("Qual o nome do 2° aluno? ")
aluno3 = input("Qual o nome do 3° aluno? ")
aluno4 = input("Qual o nome do 4° aluno? ")
alunos = [aluno1, aluno2, aluno3, aluno4]
sortiado = random.choice(alunos)
print("O aluno sorteado foi: ", sortiado)