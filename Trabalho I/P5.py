# P5: Considere o enunciado: A probabilidade de que Joãozinho resolva este
# problema é 0,5. A probabilidade de que Mariazinha resolva este problema é 0,7.
# Faça uma solução que solucione problemas iguais ao enunciado visando a
# probabilidade do problema ser resolvido se ambos tentarem independentemente?

#1 - Resolvendo o caso padrão


Joaozinho = 0.5
Mariazinha = 0.7

probabilidade_JM = (1 - Joaozinho) * (1 - Mariazinha) #Calculo a % deles falharem (AMBOS *)
print(f"PROBABILIDADE DO PROBLEMA SER RESOLVIDO É DE: {(1 - probabilidade_JM) * 100}")

print(f"-"*50)

#2 - Caso genérico
qtd_casos = int(input("Insira quantos casos quer adicionar: "))

probabilidade_falha = 1
for i in range (1, qtd_casos+1):
    valor = float(input(f"Insira o valor para o {i}º caso: "))
    probabilidade_falha *= (1 - valor)
print(f"PROBABILIDADE DO PROBLEMA SER RESOLVIDO É DE: {(1 - probabilidade_falha) * 100}%")