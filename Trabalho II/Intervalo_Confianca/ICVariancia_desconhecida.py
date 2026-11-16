import math

#Com a variância desconhecida usamos a distribuição t de Student, como uma estimativa para os valores

n = 25 #Gl = 25 - 1 = 24
dp_amostra = 10
zt = 2.797
media = 100

erro = zt * (dp_amostra / math.sqrt(n))
print(erro)

print(f"{media - erro:.3f} =< u >= {media + erro:.3f}")

def ICVarianciaDesconhecida(desvio, amostra, zstudent, media_amostral):
    erro = zstudent * (desvio / (math.sqrt(amostra)))
    print(f"{media_amostral - erro:.3f} =< u >= {media_amostral + erro:.3f}")
