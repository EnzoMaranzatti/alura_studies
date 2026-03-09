'''
Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo
de caracteres.

Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.
'''

def calcular_caracter(palavra):
   caracter = len(palavra)
   return caracter

palavra = input('Escrevva uma palavra ou uma frase: ')
qtd_caracter = calcular_caracter(palavra)

print(f'Sua palavra é [{palavra}] contendo {qtd_caracter} caracteres')