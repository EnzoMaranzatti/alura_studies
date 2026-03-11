'''
Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para aplicar diferentes
taxas de desconto sobre os valores das compras.

Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final
com um desconto fixo definido pelo usuário.
'''

desconto = float(input('Digite um desconto (%): '))

def calcular_preco(desconto):
   def preco_final():
     preco = float(input('Digite o preço: '))
     desconto_final = preco * (desconto / 100)
     preco_desconto = preco - desconto_final
     return preco_desconto
   return preco_final


preco_final = calcular_preco(desconto)
valor = preco_final()  # chama a função
print(f'Valor final com o desconto de {desconto}% é: R${valor:.2f}')