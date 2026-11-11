# P9: Faça um script que eu possa escolher entre as duas configurações
# apresentados nas imagens abaixo, que possa escolher a probabilidade de
# funcionamento de cada componente (probabilidade de funcionamento de 4
# componentes), e que resolva a probabilidade do sistema de funcionar.

def opcao1(c1, c2, c3, c4:float) -> float:
    c1_c2 = c1 * c2 # Chance de funcionar este ramo
    c3_c4 = c3 * c4 # Chance de funcionar este ramo
    nao_funcionar = (1 - c1_c2) * (1 - c3_c4) # Multiplicar as falhas
    return 1 - nao_funcionar # Aqui é a chance de funcionar

def opcao2(c1, c2, c3, c4: float) -> float:
    c1_c3 = (1 - c1) * (1 - c3) #Chance desse ramo em paralelo falhar
    c2_c4 = (1 - c2) * (1 - c4)    
    return  (1 - c1_c3) * (1 - c2_c4) 

while True:
    c1 = float(input("Insira C1: "))
    c2 = float(input("Insira C2: "))
    c3 = float(input("Insira C3: "))
    c4 = float(input("Insira C4: "))

    print("[1] Opção 2-2:Série, paralelo ")
    print("[2] Opção 1-1:Paralelo * 1-1:Paralelo")

    escolha = int(input("Qual sua escolha: "))

    if escolha == 1:
        resultado = opcao1(c1, c2, c3, c4) * 100
        print(f"% Dessa configuração funcionar: {resultado}")

    if escolha == 2:
        resultado = opcao2(c1, c2, c3, c4) * 100
        print(f"% Dessa configuração funcionar: {resultado}")

    print(f"-"*50)
    continuar = str(input("S / N"))
    if continuar == "N":
        break
