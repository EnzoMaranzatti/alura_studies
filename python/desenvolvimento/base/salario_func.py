import os

nome = input('Nome funcionario: ')
salario = float(input('Salario do funcionario: '))
print('Quer atribuir um aumento de salario? \n 1. Sim\n 2. Não')
op = int(input('Digite uma opção: '))
if(op == 1):
  valor_aumento = float(input('Digite um valor para o aumento: '))


def aumento(valor_aumento, salario):
  bonus_porcentagem = valor_aumento / 100
  bonus_salario = salario * bonus_porcentagem
  salario_final = salario + bonus_salario
  return salario_final

# 10 / 100 = 0.1
# 5000 * 0.1

if(op == 1):
  print(f'O funcionario {nome} recebe {salario} e teve um aumento de {valor_aumento}%, sendo seu novo salario de {aumento(valor_aumento, salario)}')
else: 
  print(f'O funcionario {nome} recebe {salario}')