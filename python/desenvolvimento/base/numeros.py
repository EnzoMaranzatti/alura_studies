import os

num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
print('\nQual tipo de operação quer realizar? \n 1. Soma\n 2. Subtração\n 3. Multiplicação\n 4. Divisão')
op = int(input('Digite a operação: '))

def somar(num1, num2):
  return num1 + num2

def subtrair(num1, num2):
  return num1 - num2

def multiplicar(num1, num2):
  return num1 * num2

def dividir(num1, num2):
  return num1 / num2

match(op):
  case 1: 
    os.system('clear')
    print(somar(num1, num2))
  case 2: 
    os.system('clear')
    print(subtrair(num1, num2))
  case 3: 
    os.system('clear')
    print(multiplicar(num1, num2))
  case 4: 
    os.system('clear')
    print(dividir(num1, num2))
  case _: 
    os.system('clear')
    print('Erro na operacão')

