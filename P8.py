# P8: Em uma fábrica de parafusos, as máquinas A, B e C produzem 25%, 35% e
# 40% do total produzido. Da produção de cada máquina, 5%, 4% e 2%,
# respectivamente, são defeituosos. Escolhe-se ao acaso um parafuso e verifica-se
# que ele é defeituoso. Qual é a probabilidade de que seja da máquina A, da máquina
# B e da máquina C?

#Teorema de bayes

qtd_maquinas = int(input("Insira a quantia de máquinas: "))
producao = []
erro = []
erro_por_maquina = []
for i in range(qtd_maquinas):
    producao.append(float(input(f"Insira EM DECIMAL a produção da {i+1}º máquina: ")))
    erro.append(float(input(f"Insira EM DECIMAL o erro da {i+1}º máquina: ")))
    
for i in range(qtd_maquinas):
    erro_por_maquina.append(producao[i] * erro[i])

total_erro = sum(erro_por_maquina)
for i in range(qtd_maquinas):
    print(f"% de ERRO da {i+1}º máquina: {(erro_por_maquina[i] / total_erro) * 100}")