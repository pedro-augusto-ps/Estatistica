# P11:Dados históricos mostram que 5% dos itens provindos de um fornecedor
# apresentam algum tipo de defeito. Considerando um lote com 20 itens, calcule a
# probabilidade de:
# a) haver algum item com defeito;
# b) haver exatamente dois itens defeituosos;
# c) haver mais de dois itens defeituosos.
# d) Qual é o número esperado de itens defeituosos no lote? E de itens bons?
# e) Qual é a variância da função de probabilidade do número de itens defeituosos no
# lote?


#Probabilidade Binomial -> combinação * p^n * (1-p)^n-k

probabilidade_defeito = 0.05
n = int(input("Insira N: "))
k = int(input("Insira o K: "))
aux = 1


def fatorial(k): #Resolve o fatorial
    if k == 0:
        return 1
    fat = k
    for i in range(1, k):
        fat *= i 
    return fat

for i in range(k):
    aux *= (n - i)
    
print("-----A, B-----")
combinacao = aux / fatorial(k)
print(combinacao)
binomial = combinacao * (pow(probabilidade_defeito, k)) 
print(binomial)
binomial = binomial * pow((1 - probabilidade_defeito),n-k) # 1 - prob_defeito = sucesso
print(binomial)
# Letras A e B respondidas com o código acima.
print("-----A, B-----\n")

print("-----C-----")
letra_c = 0
for k in range(3): # Fazemos até dois (Prob. 0+1+2) tiramos 1 disso, OBS: Pedi ajuda pra IA
    combinacao = aux / fatorial(k)
    binomial = combinacao * (pow(probabilidade_defeito, k)) 
    binomial = binomial * pow((1 - probabilidade_defeito),n-k) # 1 - prob_defeito = sucesso
    letra_c += binomial
print(f"Probabilidade de mais de dois itens defeituosos: {(1 - letra_c )* 100}%")
print("-----C-----\n")

#Letra D:
#100 - 5% = 5 itens com defeito, 95 bons
print("-----D-----")
print(f"Itens bons: {(1 - 0.05) * 20}")
print(f"Itens com não conformidade: {20 * 0.05}")
print("-----D-----\n")

# Letra E
print("-----E-----")
#formula variancia binomial = n*p*(1-p)
print(20*0.05*(1-0.05))
