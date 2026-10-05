# P3: De um conjunto de cinco empresas, deseja-se selecionar, aleatoriamente, uma
# empresa, mas com probabilidade proporcional ao número de funcionários. O
# número de funcionários da Empresa A é 20; de B é 15; de C é 7; de D é 5 e de E é
# 3. 
# Faça usando variáveis.
# a) Qual é a probabilidade de cada uma das empresas ser a selecionada?
# b) Qual é a probabilidade de a Empresa A não ser selecionada?

A, B, C, D, E = 20, 15, 7, 5, 3
total = (A + B + C + D +E)
prob_A = (A / total) * 100
prob_B = (B / total) * 100
prob_C = (C / total) * 100
prob_D = (D / total) * 100
prob_E = (E / total) * 100

#Não ser selecionado = 1 - ser selecionada
total_prob = (prob_A + prob_B + prob_C + prob_D + prob_E)
prob_naoA = total_prob - prob_A
#OU = 100 - probA

print(f"PROBABILIDADE DE A: {prob_A}%")
print(f"PROBABILIDADE DE B: {prob_B}%")
print(f"PROBABILIDADE DE C: {prob_C:.2f}%")
print(f"PROBABILIDADE DE D: {prob_D}%")
print(f"PROBABILIDADE DE E: {prob_E}%")
print(f"-"*50)
print(f"PROBABILIDADE DE NÃO SER A: {prob_naoA}%")