# P19: Faça um script que, baseado em uma variável com distribuição normal de
# média (μ = Me) e (σ = Dp), possa calcular a probabilidade do evento acontecer em
# intervalos (entre intervalos, menor que e maior que). Use Me=48 e Dp=3 e os
# seguintes anunciados como teste:
# a) a probabilidade do evento ter valores entre 42 e 49 cm;
# b) a probabilidade do evento ter valores superiores a 52 cm;
# c) a probabilidade do evento ter valores inferiores a 45 cm;

import math

def transformarZ(x, media, desvio):
    z = (x - media) / desvio
    return z

def ZparaProb(z):
    return 0.5  * (1 + math.erf(z / math.sqrt(2)))

while True:
    try:
        media = float(input("Insira o valor para a média: "))
        desvio = float(input("Insira o valor para o desvio padrão: "))
        if desvio <= 0:
            print("Valor para desvio padrão inválido")
            continue
        opcoes = int(input("[1] Valor ENTRE, [2] Valor SUPERIOR, [3] Valor INFERIOR"))
    except ValueError:
        print("Por favor, insira valores válidos")
        continue
    print("-" * 50)
    if opcoes == 1:
        try:
            Linf = float(input("Insira o limite inferior: "))
            Lsup = float(input("Insira o limite superior: "))
        except ValueError:
            print("Por favor, insira valores válidos")
            continue
        z_inf = transformarZ(Linf, media, desvio)
        z_sup = transformarZ(Lsup, media, desvio)
        prob = ZparaProb(z_sup) - ZparaProb(z_inf)
        print(f"Probabilidade: {prob * 100:.4f}%")
    
    elif opcoes == 2:
        try:
            limite = float(input("Insira o limite: "))
        except ValueError:
            print("Por favor, insira valores válidos")
            continue
        z_limite = transformarZ(limite, media, desvio)
        prob = 1 - ZparaProb(z_limite)
        print(f"Probabilidade: {prob * 100:.4f}%")

    elif opcoes == 3:
        try:
            limite = float(input("Insira o limite: "))
        except ValueError:
            print("Por favor, insira valores válidos")
            continue
        z_limite = transformarZ(limite, media, desvio)
        prob = ZparaProb(z_limite)
        print(f"Probabilidade: {prob * 100:.4f}%")

    else:
        print("Opção inválida")
        continue

    continuar = input("Deseja continuar? S/N" ).upper()
    if continuar == "N":
        break
    else:
        print(f"{"-"*50} \n")
        continue

