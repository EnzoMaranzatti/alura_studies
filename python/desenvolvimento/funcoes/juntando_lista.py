'''
Clara está gerenciando o estoque de sua loja e recebeu duas listas separadas: uma contendo os nomes dos produtos e outras
com seus respectivos preços. Para facilitar a organização, ela precisa combinar essas listas de forma que cada produto seja 
associado ao seu preço.

Crie um programa que junte as listas e exiba o resultado no formato produto: preço


Digite os produtos separados por vírgula: maçã, banana, pera  

Digite os preços separados por vírgula: 2.5, 1.2, 3.0 
'''

def juntar_lista():
   produtos = input('Digite o produtos separados por vírgula: ').strip().split(',')
   precos = [float(p) for p in input('Digite os preços separados por vírgula: ').strip().split(',')]

   for produto, preco in zip(produtos, precos):
      print(f'{produto}: R${preco:.2f}')

juntar_lista()



