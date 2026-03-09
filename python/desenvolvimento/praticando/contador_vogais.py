'''
Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em um texto 
digitado pelos alunos. Isso ajudará a analisar a estrutura das palavras utilizadas.

Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.
'''

vogais = ('a', 'e', 'i', 'o', 'u')
qtd_vogais = 0


texto = input('Digite o texto que deseja calcular vogais: ').lower().strip()

for vagais in texto:
   if vagais in texto:
      qtd_vogais += 1

print(f'Texto:\n{texto}\n\nQuantida de vogais: {qtd_vogais}')