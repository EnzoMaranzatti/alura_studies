'''
Carlos está criando uma calculadora simples, mas quer garantir que o programa não quebre se o usuário 
digitar valores inválidos, ele precisa tratar os erros.

Crie uma calculadora que permita ao usuário escolher entre soma, subtração, multiplicação e divisão. 
Além de modularizar o código em funções, use try-except para tratar erros de entrada inválida, que consiste em:

Caso digite um caractere em vez de número | exceção a ser lançada: ValueError;
Caso tente fazer uma divisão por 0 | exceção a ser lançada: ZeroDivisionError.
'''

OPERACOES = ('+', '-', '/', '*')
somar = lambda num1, num2: num1 + num2
subtrair = lambda num1, num2: num1 - num2
dividir = lambda num1, num2: num1 / num2
multiplicar = lambda num1, num2: num1 * num2

def veriricar_operacao(operacao):
   operarao_valida = False
   if operacao in OPERACOES:
      operarao_valida = True
   
   return operarao_valida

def pedir_numero(mensagem):
   while True:
      try:
         return float(input(mensagem))
      except ValueError:
         print('Número inválido! Digite um número.')

def dividir(num1, num2):
   try:
      return num1 / num2
   except ZeroDivisionError:
      print('Erro: divisão por zero!')
      return None

def calculo():
   num1 = pedir_numero('Digite o primeiro número: ')
   operacao = input('Digite a operação desejada (+, -, /, *): ')

   if veriricar_operacao(operacao):
      num2 = pedir_numero('Digite o segundo número: ')

      match operacao:
         case '+': valor_final = somar(num1, num2)
         case '-': valor_final = subtrair(num1, num2)
         case '/': valor_final = dividir(num1, num2)
         case '*': valor_final = multiplicar(num1, num2)

      if valor_final is not None:
         print(f'{num1} {operacao} {num2} = {valor_final}')
   else:
      print('Operação inválida!')

calculo()


