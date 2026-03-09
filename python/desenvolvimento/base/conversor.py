import os

num = float(input('Digite um metro: '))
print('''\nDeseja converter para qual opção:
      1. Centimetro
      2. Milimetro''')
op = int(input('Digite uma opção: '))

def convertC(num):
  return num * 100

def convertMM(num):
  return num * 1000

match op:
  case 1:
    os.system('clear')
    print(f'Resultado: {num} metros = {convertC(num)} centimetros')
  case 2:
    os.system('clear')
    print(f'Resultado: {num} metros = {convertMM(num)} milimetros')
  case _: print('Erro de opção...')