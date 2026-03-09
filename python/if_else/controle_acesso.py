'''
Mariana é responsável por liberar o acesso ao escritório e precisa de um programa que verifique se os funcionários podem entrar.
Para isso, ela usará o horário atual. O escritório só permite acesso entre 8h e 18h. Crie um programa que receba a hora atual
como entrada (em formato de 24 horas) e exiba uma mensagem informando se o acesso é permitido ou negado.
'''

horario_atual = int(input('Digite o horário atual (formato 24h): '))

if 8 <= horario_atual <= 18:
    print(f'Acesso liberado. Hora atual {horario_atual}')
else:
    print(f'Acesso negado. Hora atual {horario_atual}')