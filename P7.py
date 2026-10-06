# P7: Uma rede local de computadores é composta por um servidor e cinco clientes
# (A, B, C, D e E). Registros anteriores indicam que dos pedidos de determinado tipo
# de processamento, cerca de 10% vêm do cliente A, 15% do B, 15% do C, 40% do D
# e 20% do E. 
# Se o pedido não for feito de forma adequada, o processamento
# apresentará erros. Usualmente, ocorrem os seguintes percentuais de pedidos
# inadequados: 1% do cliente A, 2% do cliente B, 0,5% do cliente C, 2% do cliente D e
# 8% do cliente E.

# a) Qual é a probabilidade de o sistema apresentar erro?
# b) Qual é a probabilidade de que o processo tenha sido pedido pelo cliente E,
# sabendo que apresentou erro?

print("---Teorema de Bayes---")

erroA = 0.10 * 0.01  #0.10 do pedido ser do A e 0.01 do A apresentar erro
erroB = 0.15 * 0.02
erroC = 0.15 * 0.005
erroD = 0.40 * 0.02
erroE = 0.20 * 0.08
total_erros = (erroA + erroB + erroC + erroD + erroE)
print(f"Probabilidade do sistema todo apresentar erros: {total_erros * 100}%")

processoE = erroE / total_erros
print(f"Probabilidade do erro ter sido pedido pelo cliente E, tendo apresentado erro: {processoE * 100:.2f}%")