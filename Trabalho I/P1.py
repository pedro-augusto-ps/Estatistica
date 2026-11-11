# P1: Considere que você tem 3 conjuntos com valores aleatórios (A, B, C). Faça um
# script que retorna os seguintes eventos:
# 1. (A ∪ B);
# 2. A ∩ B;
# 3. A ∩ C;
# 4. A^c(A no complementar)
import numpy as np

qtd_A = int(input("Quantos elementos irá ter o A: "))
qtd_B = int(input("Quantos elementos irá ter o B: "))
qtd_C = int(input("Quantos elementos irá ter o C: "))

A = np.random.randint(1, 10, qtd_A)
B = np.random.randint(1, 10, qtd_B)
C = np.random.randint(1, 10, qtd_C)
print(f"Vetor A: {A}")
print(f"Vetor B: {B}")
print(f"Vetor C: {C}")

#Método com funções do NP
uniao_AB = (np.union1d(A, B)) 
inter_AB = (np.intersect1d(A, B))
inter_AC = (np.intersect1d(A, C))
universo = np.union1d(uniao_AB, C)
A_comp = np.setdiff1d(universo, A)
print(f"-"*50)

print(f"Resposta 1: {uniao_AB}")
print(f"Resposta 2: {inter_AB}")
print(f"Resposta 3: {inter_AC}")
print(f"Resposta 4: {A_comp}")
print(f"-"*50)

#Método bruto
#Q = Question
q1 = []
for elemento in A:
    if elemento not in q1:
        q1.append(int(elemento))
for elemento in B:
    if elemento not in q1:
        q1.append(int(elemento))
q1 = sorted(q1)

q2 = []
for elemento in A:
    if elemento in B and elemento not in q2:
        q2.append(int(elemento))
q2 = sorted(q2)

q3 = []
for elemento in A:
    if elemento in C and elemento not in q3:
        q3.append(int(elemento))
q3 = sorted(q3)


universo1 = q1[:]
for elemento in C:
    if elemento not in universo1:
        universo1.append(int(elemento))
        
q4 = []
for elemento in universo1:
    if elemento not in A:
        q4.append(elemento)
q4 = sorted(q4)

print(f"Resposta 1: {q1}")
print(f"Resposta 2: {q2}")
print(f"Resposta 3: {q3}")
print(f"Resposta 4: {q4}")