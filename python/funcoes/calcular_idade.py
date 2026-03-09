'''
Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades
com base no ano de nascimento. Sua tarefa é criar uma função que receba o ano de nascimento 
e o ano atual e retorne à idade correspondente.
'''

def calcular_idade(ano_atual, ano_nasc):
   idade = ano_atual - ano_nasc
   return idade

ano_atual = int(input('Digite o ano atual: '))
ano_nasc = int(input('Digite o ano de nascimento: '))
idade_atual = calcular_idade(ano_atual, ano_nasc)

print(f'Você tem {idade_atual} anos de idade')


