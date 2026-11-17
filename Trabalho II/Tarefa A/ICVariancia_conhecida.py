import math
from scipy import stats

# n = Amostra
# σ = Desvio padrão populacional, raiz quadrada da variância populacional
# X̄ = Média amostral (Média amostral para calcular a média populacional)
#FÓRMULA: X̄ +- Za/2 * ( σ / √n )


def ICVarianciaConhecida(amostra, media_amostral, confianca, variancia_populacional):
    """
    PARÂMETROS:
    amostra: Deve ser maior ou igual a 1
    σ^2: Não pode ser negativa
    confianca: Deve estar entre 0 e 1,

    RETORNOS:
    Retorna um DICT com nossas respostas
    """
    distribuicao = "Z"

    if confianca <= 0 or confianca >= 1:
        raise ValueError("Confiança deve estar entre 0 e 1. [EX: 0.95]")
    if amostra < 1 or type(amostra) != int:
        raise ValueError("Valor inválido para amostra!")
    if variancia_populacional <= 0:
        raise ValueError("Variância populacional não pode ser negativa!")

    alpha = 1 - confianca
    valor_critico = stats.norm.ppf(1 - alpha / 2)

    erro = valor_critico * (math.sqrt(variancia_populacional) / (math.sqrt(amostra)))

    limite_inferior = media_amostral - erro
    limite_superior = media_amostral + erro
    return {
        "distribuicao": distribuicao,
        "margem": erro,
        "estimativa": media_amostral,
        "limite_inferior": limite_inferior,
        "limite_superior": limite_superior,
    }

    