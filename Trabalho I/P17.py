# P17: Certo tipo de conserva tem peso líquido (X1) com média de M1 g e 
# desvio-padrão de D1 g. 
# A embalagem tem peso (X2) com média de M2 g e
# desvio-padrão de D2 g. Suponha (X1) e (X2) independentes e com distribuições
# normais. Para o teste use os valores 900g, 10g, 100g e 4g respectivamente.

# a) Faça um programa que calcule a probabilidade de o peso bruto (peso líquido +
# peso da embalagem) ser superior a uma referência MS. Para o teste use o valor
# 1.020

# b) Faça um programa que calcule a probabilidade de o peso bruto estar entre um
# intervalo entre I1 e I2 g. Para teste use os valores 980 e 1.020 g    
# x1 <= P <= x2
import math
import matplotlib.pyplot as plt


x1 = float(input("Insira a média de X1: "))
desvio_x1 = float(input("Insira o desvio-padrão de X1: "))
x2 = float(input("Insira a média de X2: "))
desvio_x2 = float(input("Insira o desvio-padrão de X2: "))

media = x1 + x2 #Média das somas é a soma das médias
variancia = (desvio_x1 ** 2) + (desvio_x2 ** 2)
desvio = math.sqrt(variancia)


def transformarZ(x, media, desvio):
    z = (x - media) / desvio
    return z

def ZparaProb(z): #Pedi ajuda para IA, não entendi como fazer sem a tabela Z
    return 0.5  * (1 + math.erf(z / math.sqrt(2)))

x = float(input("insirao valor para X: ")) 
A = transformarZ(x, media, desvio) #Letra A
A_prob = 1 - ZparaProb(A) #Resposta letra A
print(f"Solução para letra A: {A_prob}")

l1 = float(input("Insirao limite inferior L1: "))
l2 = float(input("Insirao limite superior L2: "))

limites1 = transformarZ(l1, media, desvio)
limites2 = transformarZ(l2, media, desvio)
prob_limites = ZparaProb(limites2) - ZparaProb(limites1)
print(f"Probabilidade estar entre {limites1} e {limites2} é de: {prob_limites * 100}%")

