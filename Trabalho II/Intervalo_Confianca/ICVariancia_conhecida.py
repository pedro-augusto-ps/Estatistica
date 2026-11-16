import math

# n = Amostra
# σ = Desvio padrão populacional, raiz quadrada da variância populacional
# X̄ = Média amostral (Média amostral para calcular a média populacional)

#FÓRMULA: X̄ +- Za/2 * ( σ / √n )
variancia_populacional = 4.41 #Populacional pois é conhecida (Caso raro, pois é dificil estimar toda população)
amostra = 75
intervalo_confianca = 1.96
media = 4.3 #Média amostral
erro = media * (math.sqrt(variancia_populacional) / math.sqrt(amostra))

print(f"{media - erro:.3f} =< u >= {media + erro:.3f}")

def ICVarianciaConhecida(desvio, amostra, znormal, media_amostral):
    erro = znormal * (desvio / (math.sqrt(amostra)))
    print(f"{media_amostral- erro:.3f} =< u >= {media_amostral + erro:.3f}")
