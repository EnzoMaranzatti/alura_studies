import os

nome_produto = input('Nome do produto: ')
preco_produto = float(input('Preço do produto: '))
qta_produto = int(input('Quantidade produto: '))

total_preco = preco_produto * qta_produto

if total_preco >= 100:
    desconto = total_preco * 0.1
    subTotal = total_preco - desconto
    print(f'Prod.: {nome_produto} - R${preco_produto} ==== Qtd: {qta_produto} - T. Preco: {total_preco} ==== Desc.: R${desconto} - sub.t.: R${subTotal}')
else: 
    print(f'Prod.: {nome_produto} - R${preco_produto} ==== Qtd: {qta_produto} - T. Preco: {total_preco}')