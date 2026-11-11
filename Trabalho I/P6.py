# P6: Se os registros indicam que 504, dentre 813 lavadoras automáticas de pratos
# vendidas por uma grande loja de varejo, exigiram reparos dentro da garantia de um
# ano, qual é a probabilidade de uma lavadora dessa loja não exigir reparo dentro da
# garantia?

exigiram_reparo = 504
total = 813
chance_de_pedir_reparo = 504 / 813
chance_nao_reparo = (1 - chance_de_pedir_reparo) * 100
print(f"{chance_nao_reparo:.2f}%")

print(f"-" * 50)
#Genérico

try:
    qtd_reparos = int(input("Insira quantia de lavadoras que exigiram reparos: "))
    total = int(input("Insira o total de lavadoras: "))
    if qtd_reparos <= total and total != 0:
        probabilidade = (1 - (qtd_reparos / total)) * 100
        print(f"PARA O CASO GENÉRICO A PROBABILIDADE DE NÃO PEDIR REPARO É DE: {probabilidade:.2f}%")
    else:
        print("Divisão por 0")
except ValueError:
    print(f"Erro: valor inválido")