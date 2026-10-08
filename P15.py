# P15: Uma variável (X) é uniformemente distribuída no intervalo [A, B]. Faça um
# algoritmo que calcule o valor esperado e variância de (X) e a (P(C < X < D)).

#Base = b-a * y = 1
#Y = 1 / b - a # "Os valores que essa variavel aleatória pode assumir, esta entre B e A"  A < X < B

while True:
    X = int(input("Insira o valor esperado: "))
    A = int(input("Insira A:")) #Para o intervalo grande
    B = int(input("Insira B:")) #Para o intervalo grande
    C = int(input("Insira C:"))
    if C < A or C > B:
        print("Subintervalo com valor inválido")
        continue
    D = int(input("Insira D:"))
    if D < A or D > B or D < C:
        print("Subintervalo com valor inválido")
        continue

    valor_medio = (B + A) / 2 #Média
    variancia = (B -A) **2 / 12 #Pedi para IA me ajudar, 12 é "padrão" para essa questão de [A, B]
    #Variancia = Quão distante o valor esta da média
    prob_entre_CD = (D - C) / (B - A) #Calcula a chance de um valor cair entre o intervalo C e D

    print(f"Valor médio: {valor_medio}")
    print(f"Variância: {variancia}")
    print(f"Probabilidade do valor estar entre C e D: {prob_entre_CD * 100}%")


