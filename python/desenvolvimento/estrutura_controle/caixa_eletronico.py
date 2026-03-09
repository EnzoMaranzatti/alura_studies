import os 
LIMITE_DIARIO = 500
saldo = 1000
opcao = 0

def limpar_terminal():
    os.system('clear')

def menu():
    print('\nCAIXA ELETRÔNICO\n')
    print('1. Sacar dinheiro\n2. Imprimir saldo\n3. Sair')
    return int(input('\nEscolha uma opção: '))

def sacar_dinheiro(saldo):
    limpar_terminal()
    valor_saque = float(input('\nQuanto quer sacar: '))
    
    if valor_saque <= saldo and valor_saque <= LIMITE_DIARIO:
        saldo -= valor_saque
        print(f'\nSaque de R${valor_saque}')
        print(f'Seu saldo atual é R${saldo}')
    elif valor_saque > LIMITE_DIARIO:
        print(f'Saque bloqueado. Seu limite diario é de R${LIMITE_DIARIO}')
    else:
        print('\nNão é possível sacar. Saldo insuficiente!')
        print(f'Seu saldo é R${saldo}')
    
    return saldo

def imprimir_saldo(saldo):
    limpar_terminal()
    print(f'\nSeu saldo é de R${saldo}')

while opcao != 3:
    opcao = menu()

    match opcao:
        case 1:
            saldo = sacar_dinheiro(saldo)
        case 2:
            imprimir_saldo(saldo)
        case 3:
            limpar_terminal()
            print('\nEncerrando...')
        case _:
            limpar_terminal()
            print('\nOpção inválida!')


    