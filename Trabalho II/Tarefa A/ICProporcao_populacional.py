import math
from scipy import stats

#Para descobrir a proporção, usamos p^ (P chapéu)
#P^ = "interesse"
#Com P^ utilizamos novamente, da média +- erro
#FÓRMULA: media_amostral +- Zc * sqrt.((P^(1 - P^) / n))

def proporcao_populacional(amostra, confianca, interesse, N):
    distribuicao = "Z"
    fator = math.sqrt((N - amostra) / (N - 1))
    if confianca <= 0 or confianca >= 1:
        raise ValueError(f"Confiança deve estar entre 0 e 1. [EX: 0.95], sua confiança: {confianca}")
    if amostra < 1:
        raise ValueError("Valor inválido para amostra!")
    if interesse < 0 or interesse > amostra:
        raise ValueError("Valor inválido!")

    p_chapeu = interesse / amostra
    alpha = 1 - confianca
    valor_critico = stats.norm.ppf(1 - alpha / 2)

    erro = (p_chapeu * (1 - p_chapeu)) / amostra
    if N < (20 * amostra):
        resultado = (math.sqrt(erro) * fator) * valor_critico
    else:
        resultado = valor_critico * (math.sqrt(erro))
    limite_inferior = p_chapeu - resultado
    limite_superior = p_chapeu + resultado

    print("-----PROPORÇÃO POPULACIONAL-----")
    print(f"Distribuição: {distribuicao}")
    print(f"Margem: {erro}")
    print(f"Estimativa: {p_chapeu}")
    print(f"Limite_inferior: {limite_inferior}")
    print(f"Limite_superior: {limite_superior}")
    
    # return {
    #     "distribuicao": distribuicao,
    #     "margem": erro,
    #     "estimativa": p_chapeu,
    #     "limite_inferior": limite_inferior,
    #     "limite_superior": limite_superior,
    # }

