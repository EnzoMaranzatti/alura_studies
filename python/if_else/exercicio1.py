'''

Bruno gerencia um pequeno comércio e quer saber qual
produto teve o melhor desempenho de vendas no mês passado.
Ele registrou a quantidade vendida de dois 
produtos: maçãs e bananas. Agora, ele precisa escrever 
um programa que identifique e exiba qual deles teve 
maior venda.

Crie um programa que receba o número de vendas dos
dois produtos e exiba uma mensagem indicando qual 
deles vendeu mais. Se as quantidades forem iguais, 
exiba uma mensagem dizendo que houve empate.

'''

nome_produto1 = input('Digite o nome do primeiro produto: ')
nome_produto2 = input('Digite o nome do segundo produto: ')
qtd_venda_p1 = int(input(f'{nome_produto1} vendeu quantos: '))
qtd_venda_p2 = int(input(f'{nome_produto2} vendeu quantos: '))
vencedor = False
empate = False

def divisor():
   print('-' * 42)

def listaProduto(nome_produto1, nome_produto2, qtd_venda_p1, qtd_venda_p2):
   divisor()
   print(f'{'Produto'.ljust(24)} {'Quantidade'}\n')
   print(f'{nome_produto1.ljust(24)} | {qtd_venda_p1}')
   print(f'{nome_produto2.ljust(24)} | {qtd_venda_p2}\n')

def vencedor(nome_vencedor):
   mensagem = f'{nome_vencedor} tiveram mais vendas!'
   print(mensagem)
   divisor()

def empate(nome_produto1, nome_produto2):
   mensagem = f'{nome_produto1} e {nome_produto2} venderam a mesma quantidade'
   print(mensagem)
   divisor()

if qtd_venda_p1 > qtd_venda_p2:
   listaProduto(nome_produto1, nome_produto2, qtd_venda_p1, qtd_venda_p2)
   vencedor(nome_produto1)
elif qtd_venda_p2 > qtd_venda_p1:
   listaProduto(nome_produto1, nome_produto2, qtd_venda_p1, qtd_venda_p2)
   vencedor(nome_produto2)
elif qtd_venda_p1 == qtd_venda_p2:
   listaProduto(nome_produto1, nome_produto2, qtd_venda_p1, qtd_venda_p2)
   empate(nome_produto1, nome_produto2)
else:
   print('Erro!')