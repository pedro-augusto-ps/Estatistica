from ICVariancia_desconhecida import ICVarianciaDesconhecida
from ICVariancia_conhecida import ICVarianciaConhecida

#Se variancia=not none
#Se variancia=none
#Média populacional é oque tento estimar

# "EXEMPLO: Amostra: 50, variancia_populacional: 4.41, variancia_amostral: None, confianca: 0,95"

def IC_geral(amostra, media_amostral, confianca, variancia_populacional = None, variancia_amostral = None):
    if variancia_amostral is None and variancia_populacional is None: #Caso o usuário insira informações insuficientes
        raise ValueError("Insira os dados necessários.")
    if variancia_amostral != None and variancia_populacional != None: #Caso o usuário insira informações demais.
        raise ValueError("Dados demais para calcular.")
    
    if variancia_populacional is None:
        return ICVarianciaDesconhecida(amostra, variancia_amostral, media_amostral, confianca)
    elif variancia_amostral is None:
        return ICVarianciaConhecida(amostra, variancia_populacional, media_amostral, confianca)

IC_geral(50, 100, 0.95, 100, None)