'''
Você está desenvolvendo um sistema de controle de estoque para o Buscante.
Um dos requisitos é verificar a quantidade de exemplares de um livro em estoque e continuar vendendo
até que o estoque se esgote. Sempre que uma venda é realizada, o sistema deve informar o usuário e 
atualizar a quantidade disponível.

Crie um programa que simule as vendas de um livro com o estoque inicial de 5 exemplares.
O programa deve exibir a mensagem "Venda realizada! Estoque restante: <quantidade>" a cada venda e,
ao final, exibir a mensagem "Estoque esgotado".
'''

livros = [
   {"nome": "Dom Casmurro", "Quantidade": 2},
   {"nome": "O Pequeno Príncipe", "Quantidade": 7},
]

def comprar_livro(livros, nome):
    for livro in livros:
        if livro["nome"] == nome:

            while livro["Quantidade"] > 0:
                livro["Quantidade"] -= 1
                print(f'Venda realizada! Estoque restante: {livro["Quantidade"]}')

            print("Estoque esgotado")
            return

    print('Livro não encontrado em nosso estoque!!')


comprar_livro(livros, "Dom Casmurro")

