from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('Praça', 'Gourmet')

bebida_suco = Bebida('Suco de Laranja', 5.00, '500ml')
bebida_suco.aplicar_desconto()

prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()

fungi = Sobremesa('Fungi', 55.5, 'Médio')
fungi.aplicar_desconto()
acai = Sobremesa('Açai', 125, 'Grande')
acai.aplicar_desconto()

restaurante_praca.adicionar_cardapio(bebida_suco)
restaurante_praca.adicionar_cardapio(prato_paozinho)
restaurante_praca.adicionar_cardapio(fungi)
restaurante_praca.adicionar_cardapio(acai)

# print(dir(restaurante_praca)) - Mostra todos os metodos
# print(vars(restaurante_praca)) - Mostra os atributos em formatado de dicionario


def main():
   restaurante_praca.exibir_cardapio

if __name__ == '__main__':
   main()
