'''
Paulo está desenvolvendo um programa para calcular valores acumulados em um sistema financeiro.
Ele precisa somar os todos os números inteiros de 1 até n, onde n é um valor escolhido pelo usuário.

Ajude Paulo criando uma função recursiva que receba um número n e retorne a soma de todos os números inteiros de 1 até N.
'''

def somar_numeros(n):
   if n == 0:
      return 0
   return n + somar_numeros(n - 1)

n = int(input('Digite um numero: '))
print('Resultado:', somar_numeros(n))