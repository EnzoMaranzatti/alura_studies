'''
Maria está criando um jogo para seus alunos praticarem lógica e pensamento rápido. Ela quer um programa onde o computador 
escolhe um número aleatório entre 1 e 100, e o jogador tem que adivinhar qual é.

Além de garantir a jogabilidade, Maria deseja que o programa trate erros de entrada, impedindo que o usuário forneça valores 
inválidos, como letras ou números fora do intervalo permitido.

Sua tarefa é criar um programa que gere um número aleatório entre 1 e 100 e permita que o usuário tente adivinhar o número. 
O programa deve informar se o palpite é maior ou menor que o número correto, até que o usuário acerte. Se o usuário digitar um valor
inválido ou um número fora do intervalo, uma exceção ValueError deve ser lançada .

'''

import random

numero_aleatorio = random.randint(0, 100)
acertou = False

#         False
while not acertou:
   try:
      numero = int(input('Digite um numero inteiro entre (1-100): '))
      if numero < numero_aleatorio and numero <= 100:
         print('Muito baixo! Tente novamente')
      elif numero > numero_aleatorio and numero <= 100:
         print('Muito alto! Tente novamente')
      elif numero == numero_aleatorio:
         print('Você acertou! Parabens')
         acertou = True
      elif numero > 100:
         print('Entrada inválida: Número fora do intervalo! Digite um número entre 1 e 100.')
      else:
         print('numero inválido!!')
   except ValueError:
      print('Digite um numero inteiro!')




print(numero_aleatorio)