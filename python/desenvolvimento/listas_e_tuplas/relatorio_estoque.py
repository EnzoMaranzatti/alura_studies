'''
Armano trabalha com a gestão de dois estoques de mercadorias que são representados como tuplas. Agora, 
ele precisa criar um relatório unificado com os produtos dos dois estoques juntos.

Para ajudá-lo, como você criaria um programa que ler as informações dos estoques e gera um relatório com todos os produtos juntos?
'''

estoque1 = input('Produtos do estoque 1 (separados por vírgula): ').split(', ')
estoque2 = input('Produtos do estoque 2 (separados por vírgula): ').split(', ')
estoque_unidos = estoque1 + estoque2

print(f'Estoque 1 - {estoque1}')
print(f'Estoque 2 - {estoque2}')
print(f'Estoque unidos - {estoque_unidos}')
