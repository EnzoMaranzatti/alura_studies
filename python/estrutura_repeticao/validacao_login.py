'''
João está desenvolvendo um sistema de cadastro para um site de leitura. Ele precisa garantir que os usuários insiram 
um nome de usuário e uma senha válidos. As regras são as seguintes:

O nome de usuário deve ter pelo menos 5 caracteres.

A senha deve ter pelo menos 8 caracteres.
João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. 
Quando o usuário insere dados válidos, o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".

Crie um programa que implemente essa lógica usando um laço while.
'''

CARACTER_ESPECIAL = ('@', '#', '$', '%')


def validar_user(user):
    tem_tamanho = len(user) >= 5
    sem_especial = not any(c in CARACTER_ESPECIAL for c in user)
    return tem_tamanho and sem_especial


def validar_senha(senha):
    tem_tamanho = len(senha) >= 8
    tem_numero = any(c.isdigit() for c in senha)
    tem_maiusculo = any(c.isupper() for c in senha)
    tem_especial = any(c in CARACTER_ESPECIAL for c in senha)

    return tem_tamanho and tem_numero and tem_maiusculo and tem_especial


while True:
    user = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')

    if validar_user(user) and validar_senha(senha):
        print('Cadastro realizado com sucesso!')
        break
    else:
        print('Dados inválidos. Tente novamente.\n')