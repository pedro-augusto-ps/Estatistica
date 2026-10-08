# P13: Mensagens chegam a um servidor de acordo com uma distribuição de
# Poisson, com taxa média de cinco chegadas por minuto. Faça com variáveis que
# possam ser modificadas!
# a) Qual é a probabilidade de que duas chegadas ocorram em um minuto?
# b) Qual é a probabilidade de que uma chegada ocorra em 30 segundos (Use
# variáveis)?

#Fórmula para poisson: 
import math # Poderia importar o P11 mas vou usar uma biblioteca padrão para diferenciar
#e para usar o EULER
def poisson(euler, taxa_media, qtd_queremosK):
    resultado = (euler ** (-taxa_media)) * (taxa_media ** qtd_queremosK)
    resultado = resultado / math.factorial(qtd_queremosK)
    return resultado
    
euler = math.e
while True:

    especial = str(input("Sua questão tem uma condição especial? (EX: min - seg) Y/N"))

    if especial == "Y":
        taxa_media = float(input("Insira a taxa média(Lambda): "))
        tempo_base = int(input("Insira o tempo base(1M=60): "))
        tempo_alternativo = int(input("Insira o tempo alternativo(30s): "))
        qtd_queremosK = int(input("Insira a quantia que queremos(K): "))
        taxa_media = taxa_media * (tempo_alternativo / tempo_base)

    elif especial == "N":
        taxa_media = float(input("Insira a taxa média(Lambda): "))
        qtd_queremosK = int(input("Insira a quantia que queremos(K): "))

    else:
        print("Opção inválida")
        continue

    print(f"Resposta {poisson(euler, taxa_media, qtd_queremosK)*100:.2f}%")

    continuar = str(input("Deseja continuar? Y/N"))
    if continuar == "N":
        break

