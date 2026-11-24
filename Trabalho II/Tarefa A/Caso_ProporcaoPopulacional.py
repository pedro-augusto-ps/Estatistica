import math
from scipy import stats

#P^ = Proporção amostral
#P = Proporção populacional
#FÓRMULA: media_amostral +- Zc * sqrt.((P^(1 - P^) / n))

def func_ProporcaoPopulacional(amostra, confianca, interesse, N):
    """
    PARÂMETROS:
    amostra: Deve ser maior ou igual a 1.
    confianca: Deve estar entre 0 e 1.
    interrese: Deve ser maior que 0 e MENOR que a amostra.
    N: Tamanho total da população.

    RETORNOS:
    Retorna um dict, porém deixei um print para facilitar.
    """

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
        margem = math.sqrt(erro) * valor_critico
        resultado = margem * fator
    else:
        margem = valor_critico * math.sqrt(erro)
    limite_inferior = p_chapeu - margem
    limite_superior = p_chapeu + margem

    print("-----PROPORÇÃO POPULACIONAL-----")
    print(f"Distribuição: {distribuicao}")
    print(f"Margem: {erro:.4f}")
    print(f"Estimativa: {p_chapeu}")
    print(f"Limite_inferior: {limite_inferior:.4f}")
    print(f"Limite_superior: {limite_superior:.4f}")
    
    return {
        "distribuicao": distribuicao,
        "margem": margem,
        "estimativa": p_chapeu,
        "limite_inferior": limite_inferior,
        "limite_superior": limite_superior,
    }

