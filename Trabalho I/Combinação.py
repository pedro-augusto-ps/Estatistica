def combinacao(cima, baixo): 
    """Código para combinação simplificada"""
    fatorial = 1
    for i in range(1, baixo + 1):
        if cima == 0:
            break
        else:
            fatorial *= i


    fatorial_cima = 1
    for i in range(cima, cima-baixo, - 1):
        if cima == 0:
            break
        else:
            fatorial_cima *= i
    return fatorial_cima / fatorial 