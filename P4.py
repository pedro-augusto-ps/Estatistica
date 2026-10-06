# P4: Na disciplina de Estatística para cursos de Engenharia, há 30 estudantes de
# Engenharia Civil e dez de outras engenharias. Selecionam-se, aleatoriamente e sem
# reposição, n estudantes para a realização de um trabalho. Calcule a probabilidade
# de todos serem de Engenharia Civil, considerando: Faça usando variáveis.
# a) (n = 2)
# b) (n = 4)

total = 40
engenharia_civil = 30
n = int(input("Insira quantos estudantes de ENG CIVIL: "))
probabilidade = 1
for _ in range(n):
    probabilidade *= engenharia_civil / total
    engenharia_civil -= 1
    total -= 1

print(f"{probabilidade:.2f}")