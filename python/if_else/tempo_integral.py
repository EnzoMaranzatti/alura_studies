'''
Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C.
No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos 
e não calcular o total.

Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. 
Se algum valor for negativo, mostre uma mensagem informando o erro
'''
atv_a = int(input('Digite a quantidade de dias da atividade A: '))
atv_b = int(input('Digite a quantidade de dias da atividade B: '))
atv_c = int(input('Digite a quantidade de dias da atividade C: '))

if atv_a >= 0 and atv_b >= 0 and atv_c >= 0:
    tempo_total = atv_a + atv_b + atv_c
    print(f'Tempo total das atividades: {tempo_total}')
else:
    print('Valores inválidos! Dias não podem ser negativos.')