from scipy import stats

def func_VarianciaPopulacional(amostra, confianca, variancia_amostral):
    """
    PARÂMETROS:
    amostra: Deve ser maior ou igual a 1.
    s^2: Não pode ser negativa.
    confianca: Deve estar entre 0 e 1,

    RETORNOS:
    Retorna um dict, porém deixei um print para facilitar.
    """

    distribuicao = "Qui-Quadrado"

    if confianca <= 0 or confianca >= 1:
        raise ValueError("Confiança deve estar entre 0 e 1. [EX: 0.95]")
    if amostra <= 1 or not isinstance(amostra, int):
        raise ValueError("Amostra deve ser um número inteiro maior que 1!")
    if variancia_amostral < 0:
        raise ValueError("A variância amostral não pode ser negativa!")

    alpha = 1 - confianca
    gl = amostra - 1

    valor_critico_esquerda = stats.chi2.ppf(alpha / 2, df=gl)
    valor_critico_direita = stats.chi2.ppf(1 - alpha / 2, df=gl)

    # Divide pelo maior valor crítico para achar o limite inferior, e vice-versa
    limite_inferior = (gl * variancia_amostral) / valor_critico_direita
    limite_superior = (gl * variancia_amostral) / valor_critico_esquerda

    print("-----VARIÂNCIA POPULACIONAL-----")
    print(f"Distribuição: {distribuicao}")
    print(f"Valor crítico esquerdo: {valor_critico_esquerda:.4f}")
    print(f"Valor crítico direito: {valor_critico_direita:.4f}")
    print(f"Limite inferior: {limite_inferior:.4f}")
    print(f"Limite superior: {limite_superior:.4f}") 

    return {
        "distribuicao": distribuicao, 
        "estimativa": variancia_amostral,
        "valor_critico_esquerdo": valor_critico_esquerda,
        "valor_critico_direito": valor_critico_direita,
        "limite_inferior": limite_inferior,
        "limite_superior": limite_superior,
    }
