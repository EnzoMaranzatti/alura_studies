'''
Roberto está organizando sua despensa e quer verificar se determinados 
itens já estão armazenados antes de adicioná-los à lista de compras.

Ajude Roberto a criar um programa que pergunte o item desejado e verifique se ele está 
na lista de itens disponíveis na despensa. Caso o item não esteja na lista, o programa 
deve informar que ele precisa ser comprado.
'''

despensa = ['Shampoo', 'Açucar', 'Macarrão', 'Detergente', 'Refrigerante', 'Desodorante']

def listar_despensa(despensa):
   for item in despensa:
      print(item)


def verificar_disponibilidade(produto, despensa):
   if produto in despensa:
      print(f'Produto {produto} disponível!')
   else:
      print(f'Produto {produto} indisponível! Precisa comprar')

print('PRODUTOS DA DESPENSA:\n')
listar_despensa(despensa)
produto = input('\nDigite o nome do produto que deseja verificar: ')
verificar_disponibilidade(produto, despensa)