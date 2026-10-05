# P2: Imagine o caso de retirar uma carta de um baralho de 52 cartas com 4 naipes.
# Crie um script que possamos indicar o tamanho total da população (por exemplo: 52
# cartas), quantidade de grupos que a população é dividida igualmente (4 naipes) e
# que calcule a probabilidade de retirar um elemento que não faz parte de um dos
# grupo que possamos definir anteriormente (por exemplo: a carta não ser de ouros)

#Para o baralho (script mais específico)
cartas = 52
grupo = 4
qtd_por_grupo = 52 / 4 #Tratar se não for int

print(f"A chance da carta ser de ouros: {(qtd_por_grupo / cartas) * 100}%")
print(f"A chance de não ser de ouros: {((cartas - qtd_por_grupo) / cartas) * 100}%")

#Script geral

populacao = int(input("Insira o tamanho da população: "))
while True:
    grupo = int(input("Insira o tamanho do grupo: "))
    if populacao % grupo == 0:
        break
    else:
        print("Não dá grupo exato, tente novamente \n")
        continue
qtd_por_grupo1 = populacao / grupo

tipo_população = str(input("Insira o tipo da população: ")) #Fazer uma graça
tipo_grupo = str(input("Insira o tipo do grupo: ")) #EX: população casas, grupo = amarelas

print(f"Grupo específico: {(qtd_por_grupo1 / populacao) * 100}% de {tipo_grupo}")
print(f"Total exceto um grupo específico: {(populacao - qtd_por_grupo1)/populacao * 100}% {tipo_população}")
