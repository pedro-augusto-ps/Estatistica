# P12: Seja uma população com 60 mulheres e 40 homens. Sorteiam-se duas
# pessoas. Calcule a probabilidade de sair exatamente uma mulher, usando a
# hipergeométrica. Faça com variáveis que possam ser modificadas!

# • N: Tamanho total da população.
# • K: Número total de sucessos existentes na população.
# • n: Tamanho da amostra retirada (número de tentativas).
# • k: Número de sucessos desejados na amostra. (Tirado do Google)

#Vou importar o fatorial e combinação do exercício anterior

mulheres = int(input("Insira a quantia de mulheres: ")) 
homens = int(input("Insira a quantia de homens: ")) 
pessoas = mulheres + homens #N
caso_favoravel = int(input("Insira a quantia de casos favoráveis: ")) #k
qtd_retirada = int(input("Insira a quantia retirada: ")) # n

def combinacao(cima, baixo): 
    """Código para combinação simplificada"""
    fatorial = 1
    for i in range(1, baixo + 1):
        if cima == 0:
            break
        else:
            fatorial *= i
    #Faz o fatorial padrão (A parte de baixo)

    fatorial_cima = 1
    for i in range(cima, cima-baixo, - 1):
        if cima == 0:
            break
        else:
            fatorial_cima *= i
    return fatorial_cima / fatorial #Fatorial para a parte de cima, pro exemplo C de 10,2, essa
    #é a parte 10 * 9

combinacao_sucesos = combinacao(mulheres, caso_favoravel) 
combinacao_subtraçao = combinacao(pessoas - mulheres, qtd_retirada - caso_favoravel)
combinacao_populacao = combinacao(pessoas, qtd_retirada)
resultado = (combinacao_sucesos * combinacao_subtraçao) / combinacao_populacao

print(f"A chance de um resultado favorável é de: {resultado:.2f}")