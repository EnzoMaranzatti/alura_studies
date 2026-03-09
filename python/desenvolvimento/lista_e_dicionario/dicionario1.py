#1 - Crie um dicionário representando informações sobre 
# uma pessoa, como nome, idade e cidade.
# 2 - Utilizando o dicionário criado no item 1:
    # Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
    # Adicione um campo de profissão para essa pessoa;
    # Remova um item do dicionário.

import os

pessoa = {
    'nome': 'Maria Vitória de Lima Luizetti',
    'idade': 20,
    'cidade': 'Guapiaçu'
}

def clear():
    os.system('clear')

def title(texto):
    divisor = '-' * len(texto)
    print(divisor)
    print(texto.upper())
    print(divisor)
    print()

def imprimir_informacoes(pessoa):
    title('Informações da pessoa')
    print(f'{pessoa["nome"]} tem {pessoa["idade"]} e mora em {pessoa["cidade"]}')
    input('\nDigite uma tecla para voltar ao menu... ')

def atualizar_dados(pessoa):
    title('Atualizar informações')
    print('1. Nome\n2. Idade\n3. Cidade\n4. Todas\n5. Nenhuma')

    try:
        dado = int(input('Qual dado quer alterar: ').strip())
    except ValueError:
        print('Opção inválida!')
        input('\nDigite uma tecla para voltar ao menu... ')
        return

    match dado:
        case 1:
            pessoa['nome'] = input('Digite o novo nome: ').strip()

        case 2:
            try:
                pessoa['idade'] = int(input('Digite a nova idade: ').strip())
            except ValueError:
                print('Idade inválida! (use número)')
                input('\nDigite uma tecla para voltar ao menu... ')
                return

        case 3:
            pessoa['cidade'] = input('Digite a nova cidade: ').strip()

        case 4:
            pessoa['nome'] = input('Digite o novo nome: ').strip()
            try:
                pessoa['idade'] = int(input('Digite a nova idade: ').strip())
            except ValueError:
                print('Idade inválida! (use número)')
                input('\nDigite uma tecla para voltar ao menu... ')
                return
            pessoa['cidade'] = input('Digite a nova cidade: ').strip()

        case 5:
            print('Nenhuma alteração feita.')

        case _:
            print('Opção inválida!')

    input('\nDigite uma tecla para voltar ao menu... ')

def finalizar_programa():
    clear()
    print('Finalizando...')

def menu():
    print('1. Informações\n2. Editar dados\n3. Finalizar')
    try:
        return int(input('Digite uma opção: ').strip())
    except ValueError:
        return 0

def main():
    while True:
        clear()
        opcao = menu()

        match opcao:
            case 1:
                imprimir_informacoes(pessoa)
            case 2:
                atualizar_dados(pessoa)
            case 3:
                finalizar_programa()
                break
            case _:
                print('Opção inválida!')
                input('\nDigite uma tecla para tentar de novo... ')

if __name__ == '__main__':
    main()
