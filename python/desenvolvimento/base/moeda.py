import os

moeda = float(input('Insira um valor (R$): '))
print(f'Para qual moeda quer converter R${moeda}\n 1. Doller\n 2. Euro')
op = int(input('Digite uma opção: '))

def converterDoller(moeda):
  moeda_doller = moeda * 5.6
  return moeda_doller

def converterEuro(moeda):
  moeda_euro = moeda * 7.8
  return moeda_euro

match op:
  case 1:
    os.system('clear')
    print(f'R${moeda} = ${converterDoller(moeda)}')
  case 2:
    os.system('clear')
    print(f'R${moeda} = €{converterEuro(moeda)}')
