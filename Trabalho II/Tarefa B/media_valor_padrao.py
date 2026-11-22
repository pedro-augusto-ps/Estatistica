import math
from scipy import stats


def media_padrao_Z(amostra, h0, alfa, media_amostral, desvio_populacional, orientacao):
    """Utiliza-se a distribuição Z quando o desvio populacional é conhecido."""

    calculo = (media_amostral - h0) / (desvio_populacional/ math.sqrt(amostra))

    if orientacao == "bilateral":
        z_critico = stats.norm.ppf(1 - alfa / 2)
        rejeitar = abs(calculo) > z_critico #Retorna True(rejeitou) ou False
    elif orientacao == "direita":
        z_critico = stats.norm.ppf(1 - alfa)
        rejeitar = calculo > z_critico
    elif orientacao == "esquerda":
        z_critico = -stats.norm.ppf(1 - alfa) #Teste para esquerda
        rejeitar = calculo < z_critico

    if rejeitar == True:
        rejeitar = "Sim"
    else:
        rejeitar = "Não"
    return {
        "orientacao": orientacao,
        "rejeitar": rejeitar,
    }
    print(z_critico)
    print(calculo)

media_padrao_Z(25, 200, 0.05, 195, 10, "esquerda")

def media_padrao_T(amostra, h0, alfa, media_amostral, desvio_amostral, orientacao):
    """Utiliza-se a distribuição T quando o desvio populacional não é conhecido."""
    gl = amostra - 1
    if orientacao == "bilateral":
        t_critico = stats.t.ppf(1 - alfa / 2, df=gl)
    elif orientacao == "direita":
        t_critico = stats.t.ppf(1 - alfa, df=gl)
    elif orientacao == "esquerda":
        t_critico = stats.t.ppf(alfa, df=gl)

    calculo = (media_amostral - h0) / (desvio_amostral / math.sqrt(amostra))
    print(t_critico)
    print(calculo)

media_padrao_T(16, 50, 0.05, 53, 6)