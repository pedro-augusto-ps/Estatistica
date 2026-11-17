import math
from scipy import stats

#Para descobrir a proporção, usamos p^ (P chapéu)
#P^ = sucessos / amostra (Apenas isso)
#Com P^ utilizamos novamente, da média +- erro
#FÓRMULA: media_amostral +- Zc * sqrt.((P^(1 - P^) / n))

def ICProporcao_populacional(amostra, confianca, fracassos):
    p_chapeu = fracassos / amostra
    alpha = 1 - confianca
    valor_critico = stats.norm.ppf(confianca / 2)

    erro = (p_chapeu * (1 - p_chapeu)) / amostra
    erro = valor_critico * (math.sqrt(erro))
    limite_inferior = p_chapeu - erro
    limite_superior = p_chapeu + erro

    print(limite_inferior)
    print(limite_superior)

ICProporcao_populacional(400, 0.95, 80)