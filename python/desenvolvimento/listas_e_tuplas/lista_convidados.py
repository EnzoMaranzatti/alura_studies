'''
Camila adora receber amigos para jantares temáticos. Para o próximo encontro, ela quer garantir que a ordem de 
chegada seja respeitada, mas ainda precisa fazer ajustes na lista de convidados. Camila quer adicionar novos nomes 
e organizá-los em posições específicas.

Como você criaria um programa que mostre a lista inicial, permita a inserção de um novo nome em uma posição escolhida e 
exiba a lista atualizada?
'''

convidados = ['Ana', 'Pedro', 'Carlos']
print(f'Sua lista de convidados inicial: {convidados}')
novo_convidado = input('\nDigite o nome do novo convidado: ')
while True:
   try:
      posicao = int(input(f'Em qual posição você quer inserir {novo_convidado}? '))
      if posicao <= len(convidados):
         print(f'{novo_convidado} inserido na posição {posicao} com sucesso!')
         convidados.insert(posicao, novo_convidado)
         print(f'\nSua lista de convidos atualizada: {convidados}')
         break
      print(f'\nPosição inválida! Por favor insira uma posição entre 0 a {len(convidados)}')
   except:
      print('\nPor favor insira um número!')
      


