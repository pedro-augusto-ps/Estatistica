from Caso_VarianciaDesconhecida import func_VarianciaDesconhecida
from Caso_VarianciaConhecida import func_VarianciaConhecida
from Caso_ProporcaoPopulacional import func_ProporcaoPopulacional
from Caso_VarianciaPopulacional import func_VarianciaPopulacional

def IC_geral(amostra, confianca, media_amostral = None, interesse = None, variancia_populacional = None, variancia_amostral = None, N=None):
    """Essa função resolve casos de intervalo de confiança.
    
    NOME E ORDEM DOS PARÂMETROS:
    [amostra, confianca, media_amostral, interesse, variancia_populacional, variancia_amostral, N]
    Nota: confianca use valores assim: [EX: 0.90]

    COMO UTILIZAR: 
    1 - Chamada direta, porém precisa preencher todos os dados, os que não possui coloque None
    EXEMPLO: IC_geral(81, 0.95, 346, None, 20.25, None, None )
    2 - Chamada por variável na função
    EXEMPLO: IC_geral(amostra=81, confianca=0.95, media_amostral=346, variancia_populacional=20.25)
    
    ERROS:
    Erros de valores, números inválidos, informações faltantes, etc, são tratados com "Raise" 
    irá poluir um pouco seu terminal porém você conseguirá descobrir o motivo do erro (grande parte) 
    
    RETORNO:
    Um dict, você consegue observar a resposa pelo print, se deseja ou apagar."""

    if variancia_amostral is None and variancia_populacional is None and interesse is None: #Caso o usuário insira informações insuficientes
        raise ValueError("Insira os dados necessários.")
    if variancia_amostral is not None and variancia_populacional != None: #Caso o usuário insira informações demais.
        raise ValueError("Dados demais para calcular.")
    
    if variancia_populacional is None and interesse is None:
        return func_VarianciaDesconhecida(amostra, confianca, media_amostral, variancia_amostral)
    
    elif variancia_amostral is None and interesse is None:
        return func_VarianciaConhecida(amostra, confianca, media_amostral, variancia_populacional)
    
    elif interesse is not None and variancia_populacional is None:
        return func_ProporcaoPopulacional(amostra, confianca, interesse, N)
    
    elif media_amostral == None and interesse == None and variancia_populacional == None and variancia_amostral is not None:
        return func_VarianciaPopulacional(amostra, confianca, variancia_amostral)

# --CASOS DE TESTE--
# resultado = IC_geral(81, 0.95, 346, None, 20.25, None, None )
# print(resultado)
# resultado = IC_geral(amostra=81, confianca=0.95, media_amostral=346, variancia_populacional=20.25)
# print(resultado)