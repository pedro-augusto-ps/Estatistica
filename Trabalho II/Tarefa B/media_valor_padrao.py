import math
from scipy import stats

def media_padrao_Z(amostra, h0, alfa, media_amostral, desvio_populacional, orientacao):
    """Utiliza-se a distribuição Z quando o desvio populacional é conhecido."""

    estatistica_de_teste = (media_amostral - h0) / (desvio_populacional/ math.sqrt(amostra))

    if orientacao == "bilateral":
        z_critico = stats.norm.ppf(1 - alfa / 2)
        rejeitar = abs(estatistica_de_teste) > z_critico #Retorna True(rejeitou) ou False
        h1 = "!="
    elif orientacao == "direita":
        z_critico = stats.norm.ppf(1 - alfa)
        rejeitar = estatistica_de_teste > z_critico
        h1 = ">"
    elif orientacao == "esquerda":
        z_critico = -stats.norm.ppf(1 - alfa) #Teste para esquerda
        rejeitar = estatistica_de_teste < z_critico
        h1 = "<"
    else:
        raise ValueError("Orientação inválida")
    
    if rejeitar:
        rejeitar = "Sim"
    else:
        rejeitar = "Não"

    print(f"Crítico: {z_critico}")
    print(f"Estatística de teste: {estatistica_de_teste:.4f}")
    print(f"H0: u = {h0}")
    print(f"H1: u {h1} {h0}") #Gambiara para decidir o símbolo
    print(f"Rejeitar: {rejeitar}")

    return {
        "h0": f"u = {h0}",
        "h1": f"u {h1} {h0}",
        "estatistica": estatistica_de_teste,
        "critico": z_critico,
        "rejeitar": rejeitar,
    }


media_padrao_Z(25, 200, 0.05, 195, 10, "esquerda")

def media_padrao_T(amostra, h0, alfa, media_amostral, desvio_amostral, orientacao):
    """Utiliza-se a distribuição T quando o desvio populacional não é conhecido."""
    
    gl = amostra - 1
    estatistica_de_teste = (media_amostral - h0) / (desvio_amostral / math.sqrt(amostra))

    if orientacao == "bilateral":
        t_critico = stats.t.ppf(1 - alfa / 2, df=gl)
        rejeitar = abs(estatistica_de_teste) > t_critico
        h1 = "!="
    elif orientacao == "direita":
        t_critico = stats.t.ppf(1 - alfa, df=gl)
        rejeitar = estatistica_de_teste > t_critico
        h1 = ">"
    elif orientacao == "esquerda":
        t_critico = stats.t.ppf(alfa, df=gl)
        rejeitar = estatistica_de_teste < t_critico
        h1 = "<"
    else:
        raise ValueError("Orientação inválida")

    if rejeitar:
        rejeitar = "Sim"
    else:
        rejeitar = "Não"
    
    print(f"Crítico: {t_critico}")
    print(f"Estatística de teste: {estatistica_de_teste:.4f}")
    print(f"H0: u = {h0}")
    print(f"H1: u {h1} {h0}") #Gambiara para decidir o símbolo
    print(f"Rejeitar: {rejeitar}")

    return {
        "h0": f"u = {h0}",
        "h1": f"u {h1} {h0}",
        "estatistica": estatistica_de_teste,
        "critico": t_critico,
        "rejeitar": rejeitar,
    }

media_padrao_T(16, 50, 0.05, 53, 6, "direita")