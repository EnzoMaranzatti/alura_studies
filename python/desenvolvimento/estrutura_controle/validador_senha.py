import os
CARACTER_ESPECIAL = ('@', '#', '$', '%')

def validacao_senha(senha):
    tem_tamanho = len(senha) >= 8
    tem_numero = any(c.isdigit() for c in senha)
    tem_maiusculo = any(c.isupper() for c in senha)
    tem_especial = any(c in CARACTER_ESPECIAL for c in senha)
    
    return tem_tamanho and tem_numero and tem_maiusculo and tem_especial
    
while True:
    senha = input('Digite uma senha: ')
    
    if validacao_senha(senha):
        os.system('Clear')
        print(f'Sua senha está forte {senha}')
        break
    else:
        print('Sua senha está fraca. Tente novamente ')

    