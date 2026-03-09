''''
Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. 
Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.
'''

temperatura = float(input('Digite a temperatura atual da sala: '))

if temperatura == 25:
   print(f'Alerta!! A temperatura está no limite {temperatura}°C / 25°C')
elif temperatura > 25:
   print(f'Alerta!! A temperatura ultrapassou o limite de segurança {temperatura}°C / 25°C')
else:
   print(f'Temperatura está estável {temperatura}°C')