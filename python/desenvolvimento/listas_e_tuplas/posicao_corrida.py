'''
O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final dos participantes. 
Mas, um erro foi identificado: um dos nomes está incorreto. O organizador precisa de um programa que permita localizar 
o nome errado e substituí-lo pelo correto.

Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a lista exibindo a 
nova classificação ao final?
'''
participantes = ['Ana', 'Carlos', 'João', 'Marina']

def alterar_nome(nome_errado, nome_correto):
    indice = participantes.index(nome_errado)
    participantes[indice] = nome_correto

print('Classificação atual:')
print(participantes)

nome_errado = input('\nDigite o nome que está errado: ').strip()
nome_correto = input('Digite o nome correto: ').strip()

alterar_nome(nome_errado, nome_correto)

print('\nClassificação atualizada:')
print(participantes)
