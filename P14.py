# P14: Em um canal de comunicação digital, a probabilidade de receber um bit com
# erro é de 0,0002. Se 10.000 bits forem transmitidos por esse canal, qual é a
# probabilidade de que mais de 4 bits sejam recebidos com erro? Faça com variáveis
# que possam ser modificadas
from Combinação import combinacao

class Probabilidade():
    def __init__(self, qtd_bits, probabilidade_erro, bits_jogados):
        self.qtd_bits = qtd_bits #
        self.probabilidade_erro = probabilidade_erro
        self.bits_jogados = bits_jogados 

    def binomial(self):
        combina= combinacao(self.qtd_bits, self.bits_jogados) 
        calculo = combina * (self.probabilidade_erro ** self.bits_jogados) #Probabilidade do erro
        calculo = calculo * (1 - self.probabilidade_erro)**(self.qtd_bits - self.bits_jogados)
        return calculo

    def maior_que(self):
        """Para questões quando você quer saber "MAIS QUE" Exemplo:
        Quero saber mais que 4: insira 4 no limite então"""

        limite = int(input("Insira a quantia de bits limite que você quer saber o limite: "))
        acumulador = 0
        for i in range(limite + 1):
            self.bits_jogados = i #Sim, isso muda o atributo da classe inteira :D Perdoa o pai
            acumulador += self.binomial()
        return 1 - acumulador 
conta1 = Probabilidade(10000, 0.0002, 4)

print(f"A probabilidade de ter erros neste limite é de: {conta1.maior_que()*100}%")

