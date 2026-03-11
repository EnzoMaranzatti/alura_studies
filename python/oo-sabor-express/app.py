from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiano')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)

# print(dir(restaurante_praca)) - Mostra todos os metodos
# print(vars(restaurante_praca)) - Mostra os atributos em formatado de dicionario

restaurante_praca.alternar_estado()


def main():
   Restaurante.listar_restaurantes()

if __name__ == '__main__':
   main()
