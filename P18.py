# P18: Faça um script que, seja (Z) uma variável aleatória com distribuição normal
# padrão, calcule o valor entre intervalos. Use os seguintes valores para teste:

# a) (P(0 < Z < 1,73))
# b) (P(0,81 < Z < +∞))
# c) (P(-1,25 ≤ Z ≤ -0,63))
import math 

def ZparaProb(z): #Pedi ajuda para IA, não entendi como fazer sem a tabela Z
    return 0.5  * (1 + math.erf(z / math.sqrt(2)))


while True:

    infinito = str(input("Tem algum valor tendendo ao infinito? S/N "))
    if infinito == "S":
        qual_Z = str(input("Ele tende para qual lado? ESQ / DIR "))
        if qual_Z == "DIR":
            primeiro_z = float(input("Insira o primeiro Z: "))
            inf_dir = 1 - ZparaProb(primeiro_z)
            print(f"Resposta: {inf_dir}")

        elif qual_Z == "ESQ":
            ultimo_z = float(input("Insira o último Z: "))
            inf_esq = ZparaProb(ultimo_z)
            print(f"Resposta: {inf_esq}")
        else:
            print("Opção inválida")

    elif infinito == "N":
        ultimo_z = float(input("Insira o último Z: "))
        primeiro_z = float(input("Insira o primeiro Z: "))
        resposta = ZparaProb(ultimo_z) - ZparaProb(primeiro_z)
        print(f"A probabilidade de estar entre {primeiro_z} e {ultimo_z}: {resposta}")
    else:
        print("Opção inválida")



