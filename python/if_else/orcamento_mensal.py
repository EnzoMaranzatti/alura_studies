'''
Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. Ele estabeleceu um limite de R$ 3.000,00 
para seus gastos e precisa de um programa que ajude a controlar suas despesas. O programa deve receber o total de despesas
realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.
'''

LIMITE = 3000

despesa = float(input('Digite sua despesa total desse mês: '))
if despesa > LIMITE:
   print(f'Você ultrapassou o limite estabelecido de R${LIMITE}, gastando R${despesa - LIMITE} a mais')
elif despesa == LIMITE:
   print(f'Você chegou ao limite estabelecido de R${LIMITE}')
else:
   print(f'Você está dentro do limite estabelecido de R${LIMITE}, com uma despesa de R${despesa}, podendo gastar ainda R${LIMITE - despesa}')