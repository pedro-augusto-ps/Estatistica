# P16: Os tempos até a falha de um dispositivo eletrônico seguem o modelo
# exponencial, com uma taxa de falha (lambda = “A” falhas/hora). Indique qual a
# probabilidade de um dispositivo escolhido ao acaso sobreviver a C horas? E a D
# horas? Para testar use A = 0,012, C=50 e D=100

# "DURAR A" = Sobrevivência
# f(x) = E^-λ * X
import math
import matplotlib.pyplot as plt

lambda1 = 0.012
C = 50
D = 100
calculoC = (math.e ** (- lambda1 * C))
calculoD = (math.e ** (- lambda1 * D))
print(f"Probabilidade de durar até C: {calculoC * 100}%")
print(f"Probabilidade de durar até D: {calculoD * 100}%")

