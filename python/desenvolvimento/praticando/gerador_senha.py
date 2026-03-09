''''
Pedro está desenvolvendo um sistema de cadastro e precisa gerar senhas seguras para os usuários. 
Ele quer um programa que crie senhas aleatórias com letras maiúsculas, minúsculas, números e caracteres 
especiais.

Crie um programa que gere uma senha aleatória de 12 caracteres, contendo pelo menos uma letra maiúscula, 
uma minúscula, um número e um caractere especial. Exiba a senha gerada.
'''

import secrets
import string

tamanho = 20

def gerar_senha(tamanho):
   #                      Todas as letras        Numero 0-9      Todos os caracteres especias
   caracteres_possiveis = string.ascii_letters + string.digits + string.punctuation
   # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

   return ''.join(secrets.choice(caracteres_possiveis) for _ in range(tamanho))


print(gerar_senha(tamanho))