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

tempos = list(range(0, 3000))

# 2. Calcular a probabilidade para cada tempo da lista
probabilidades = [math.exp(-lambda1 * t) for t in tempos]

# 3. Plotar a linha da curva
plt.plot(tempos, probabilidades, label="Curva de Sobrevivência", color="blue")

# 4. Destacar os pontos C e D no gráfico com bolinhas vermelhas
plt.scatter([C, D], [calculoC, calculoD], color="red", zorder=5, label="Pontos C e D")

# Estética do gráfico
plt.title("Modelo Exponencial - Confiabilidade do Dispositivo")
plt.xlabel("Tempo (horas)")
plt.ylabel("Probabilidade de Sobrevivência")
plt.legend()
plt.grid(True)

# Exibir a janela do gráfico
plt.show()