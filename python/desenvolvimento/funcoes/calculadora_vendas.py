'''
Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia. As vendas são informadas em
uma única linha separadas por espaços.

Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.
'''

def total_vendas():
   vendas = input('Digite o valor das suas vendas separado por espaço: ').strip()
   lista_vendas = vendas.split()
   lista_vendas_final = []

   for venda in lista_vendas:
      lista_vendas_final.append(float(venda))

   valor_final_vendas = 0

   for venda in lista_vendas_final:
      valor_final_vendas += venda
   
   print('Suas vendas:\n')
   print(lista_vendas_final)
   print(f'\nValor total de vendas: R${valor_final_vendas}')

total_vendas()