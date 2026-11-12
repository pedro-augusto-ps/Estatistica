import math

# n = Amostra
# σ = Desvio padrão populacional, raiz quadrada da variância populacional
# X̄ = Média amostral (Média amostral para calcular a média populacional)

#FÓRMULA: X̄ +- Za/2 * ( σ / √n )
dp = 2.1
n = 75
Z = 1.96
media = 4.3
erro = Z * (dp / math.sqrt(n))

print(f"{media - erro:.3f} =< u >= {media + erro:.3f}")