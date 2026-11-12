#Para σ grande
# X/ +- Zc * (σ / sqrt(n))
import math


# CÓDIGO PARA MÉDIA AMOSTRAL

# dp = float(input("Insira o DP"))
# N = float(input("Insira N"))
# Z = float(input("Insira o Zc"))
dp = 4
N = 100
Z = 1.96
media = 24
erro = (Z * dp) / math.sqrt(N)

print(erro)
print(f"{media - erro} =< u(Média populacional = calculada com todos elementos da população) >= {media + erro}")