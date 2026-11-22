from ICVariancia_desconhecida import variancia_desconhecida
from ICVariancia_conhecida import variancia_conhecida
from ICProporcao_populacional import proporcao_populacional
from ICVariancia_populacional import icvariancia_populacional

def IC_geral(amostra, confianca, media_amostral = None, interesse = None, variancia_populacional = None, variancia_amostral = None, N=None):
    """Essa função resolve casos de intervalo de confiança.
    
    NOME E ORDEM DOS PARÂMETROS:
    [amostra, confianca, media_amostral, interesse, variancia_populacional, variancia_amostral, N]

    COMO UTILIZAR: 
    1 - Chamada direta, porém precisa preencher todos os dados, os que não possui coloque None
    EXEMPLO: IC_geral(81, 0.95, 346, None, 20.25, None, None )
    2 - Chamada por variável na função"""
    if variancia_amostral is None and variancia_populacional is None and interesse is None: #Caso o usuário insira informações insuficientes
        raise ValueError("Insira os dados necessários.")
    if variancia_amostral != None and variancia_populacional != None: #Caso o usuário insira informações demais.
        raise ValueError("Dados demais para calcular.")
    
    if variancia_populacional is None and interesse is None:
        return variancia_desconhecida(amostra, confianca, media_amostral, variancia_amostral)
    
    elif variancia_amostral is None and interesse is None:
        return variancia_conhecida(amostra, confianca, media_amostral, variancia_populacional)
    
    elif interesse is not None and proporcao_populacional is None and variancia_populacional is None:
        return proporcao_populacional(amostra, confianca, variancia_populacional, interesse)
    
    elif media_amostral == None and interesse == None and variancia_populacional == None and variancia_amostral is not None:
        return icvariancia_populacional(amostra, confianca, variancia_amostral)

#Aqui você coloca os valores que tem, como calcula de forma geral, os valores que não precisa você coloca None
# -----ORDEM DOS PARÂMETROS-----
# Amostra, Confianca(EX: 0.95), media_amostra, interesse(Para proporção), variancia_populacional, variancia_amostral, N(Para proporção)


resultado = IC_geral(81, 0.95, 346, None, 20.25, None, None )
print(resultado)
resultado = IC_geral(36, 0.99, 98, None, None, 16, None)
resultado = IC_geral(amostra=81, confianca=0.95, media_amostral=346, variancia_populacional=20.25)
print(resultado)