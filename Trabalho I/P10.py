# P10: Certo tipo de conserva tem peso líquido médio de 900 g, com desvio-padrão
# de 10 g. A embalagem tem peso médio de 100 g, com desvio padrão de 4 g.
# Suponha que o processo de enchimento das embalagens controla o peso líquido, de
# tal forma que se possa supor independência entre o peso líquido e o peso da
# embalagem. Quais são a média e o desvio-padrão do peso bruto? Faça utilizando
# variáveis que podem ser modificadas e geradas automaticamente a média e o
# desvio padrão.
import math

p_liquido = 900
dp = 10
p_emb = 100
dp_emb = 4

md = p_liquido + p_emb
soma_variancia = (dp**2) + (dp_emb**2)
dp_medio = math.sqrt(soma_variancia)

#Genérico:

while True:
    peso_liquido = float(input("Insira o peso líquido: "))
    desvio_1 = float(input("Insira o primeiro desvio padrão: "))
    peso_embalagem = float(input("Insira o peso da embalagem: "))
    desvio_2 = float(input("Insira o segundo desvio padrão: "))

    media = peso_embalagem + peso_liquido
    variancia = pow(desvio_1, 2) + pow(desvio_2,2)
    desvio_padrao = math.sqrt(variancia)

    print(f"Média: {media}")
    print(f"Desvio padrão: {desvio_padrao}")

    continuar = str(input("Continuar com novos valores? Y / N: "))
    if continuar == "N":
        break
    else:
        continue