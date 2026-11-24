import math
from scipy import stats

def duas_medias_conhecidas(n1, n2, sigma1, sigma2, x1, x2, alfa, orientacao):

    calculo = ((sigma1 ** 2) / n1) + ((sigma2 ** 2) / n2)
    calculo = math.sqrt(calculo)

    estatistica_de_teste = ((x1 - x2) - 0) / calculo
    print(estatistica_de_teste)

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
    print(f"H0: u1 - u2 = 0")
    print(f"H1: u1 - u2 {h1} 0") #Gambiara para decidir o símbolo
    print(f"Rejeitar: {rejeitar}")

    return {
        "h0": f"u1 - u2 = 0",
        "h1": f"u1 - u2 {h1} 0",
        "estatistica": estatistica_de_teste,
        "critico": z_critico,
        "rejeitar": rejeitar,
    }

duas_medias_conhecidas(50, 40, 2500, 3000, 24000, 26000, 0.04, "bilateral")