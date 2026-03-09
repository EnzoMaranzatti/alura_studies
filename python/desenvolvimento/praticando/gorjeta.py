'''
João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao 
pagar a conta. O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos.

Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem 
de gorjeta desejada e exiba o valor final que o cliente deverá pagar.

Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. O programa deve calcular
e exibir o valor da gorjeta e o total a ser pago.
'''

'''

INPUTS:
   - valor_conta (float)
   - gorjeta (string)
   - resposta_sim (tupla)
   - deu_gorjeta (bool)
   - Valor Gorjeta (float)
   - Valor Final (float)

OUT:
   - Valor Final

'''
resposta_sim = ('sim', 's')

def verificar_gorjeta(gorjeta):
   return gorjeta in resposta_sim

def out(nome_cliente, valor_conta, gorjeta):
   if verificar_gorjeta(gorjeta):
      porcentagem_gorjeta = float(input(f'{nome_cliente} quantos porcento deseja dar de gorjeta?: '))
      valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100)
      valor_total = valor_conta + valor_gorjeta
      print(f'DETALHES DO CONTA DE {nome_cliente} \nValor da conta: R${valor_conta:.2f}\nValor da gorjeta: R${valor_gorjeta:.2f}\nValor total da conta: R${valor_total:.2f}')
   else: 
      print(f'\n\nDETALHES DO CONTA DE {nome_cliente.upper()} \nValor da conta: R${valor_conta:.2f}\nValor da gorjeta: Cliente não deu nenhuma gorjeta\nValor total da conta: R${valor_conta:.2f}')

def pedido():
   nome_cliente = input('Digite o nome do cliente: ')
   valor_conta = float(input(f'Quanto ficou a conta de {nome_cliente}: '))
   gorjeta = input(f'{nome_cliente} deseja dar uma gorjeta? (Sim/Não): ').lower().strip()

   out(nome_cliente, valor_conta, gorjeta)

pedido()