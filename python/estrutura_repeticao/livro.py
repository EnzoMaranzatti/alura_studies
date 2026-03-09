'''
José está desenvolvendo uma funcionalidade no sistema do Buscante para interromper a busca assim que um livro específico
é encontrado. A lista de livros já cadastrados no sistema é a seguinte:

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

Ajude José a criar um programa que percorra a lista e exiba a mensagem "Livro encontrado: <nome do livro>" 
assim que o livro "O Hobbit" for encontrado. Após encontrar o livro, o programa deve parar imediatamente a busca, 
sem verificar os livros restantes.
'''

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

def pesquisar_livro(livros, pesquisa):
   encontrado = False
   for livro in livros:
      if livro == pesquisa:
         encontrado = True
         print(f'Livro encontrado!! {livro}')
         break
      if not encontrado:
         print('Livro não encontrado em nosso estoque!!') 

nome_livro = input('Digite o nome do livro que está buscando: ')
pesquisar_livro(livros, nome_livro)