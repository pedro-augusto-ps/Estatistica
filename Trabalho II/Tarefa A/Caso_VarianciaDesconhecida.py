import math
from scipy import stats

#Com a variância desconhecida utilizamos a distribuição Z para casos em que n > 30
#Ou se n for pequeno utilizamos a distribuição T.

def func_VarianciaDesconhecida(amostra, confianca, media_amostral, variancia_amostral):
    """
    PARÂMETROS:
    amostra: Deve ser maior ou igual a 2, devido ao GL.
    s^2: Não pode ser negativa.
    confianca: Deve estar entre 0 e 1.

    RETORNOS:
    Retorna um dict, porém deixei um print para facilitar.
    """

    if confianca <= 0 or confianca >= 1:
        raise ValueError("Confiança deve estar entre 0 e 1. [EX: 0.95]")
    if amostra < 2 or type(amostra) != int:
        raise ValueError("Valor inválido para amostra!")
    if variancia_amostral < 0:
        raise ValueError("Variância amostral não pode ser negativa!")
    
    
    alpha = (1 - confianca)
    distribuicao = "T"
    if amostra > 30: 
        valor_critico = stats.norm.ppf(1 - alpha / 2)
        distribuicao = "Z"
    else:
        valor_critico = stats.t.ppf(1 - alpha / 2, df=amostra - 1) 

    erro = valor_critico * (math.sqrt(variancia_amostral) / (math.sqrt(amostra)))
    
    limite_inferior = media_amostral - erro
    limite_superior = media_amostral + erro

    print("-----VARIÂNCIA DESCONHECIDA-----")
    print(f"Distribuição: {distribuicao}")
    print(f"Margem: {erro:.4f}")
    print(f"Estimativa: {media_amostral}")
    print(f"Limite_inferior: {limite_inferior:.4f}")
    print(f"Limite_superior: {limite_superior:.4f}") 

    return {
        "distribuicao": distribuicao,
        "margem": erro,
        "estimativa": media_amostral,
        "limite_inferior": limite_inferior,
        "limite_superior": limite_superior,
    }

    