'''
Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio 
técnico de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números.

Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador 
matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.
'''

def calculadora():
   a = float(input('Primeiro número: '))
   b = float(input('Segundo número: '))
   op = input('Operador (+, -, *, /): ')

   operacoes = {
      '+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y if y != 0 else 'Erro: divisão por zero'
   }

   if op in operacoes:
      resultado = operacoes[op](a, b)
      print('Resultado:', resultado)
   else:
      print('Operador inválido')

calculadora()