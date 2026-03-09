import os

nome = input('Seu nome: ')
idade = int(input('Sua idade: '))
print('\nQual a classificação do filme: L, 10, 12, 14, 16, 18')
classificacao = input('Digite a classificação: ').upper()

# match classificao_filme:
#     case 'L': 
#       os.system('clear')
#       print('Você está livre para assistir o filme')
#     case '10': 
#       os.system('clear')
#       print("Você está livre para assistir o filme" if idade >= 10 else "Não pode participar da sessão!")
#     case '12': 
#       os.system('clear')
#       print("Você está livre para assistir o filme" if idade >= 12 else "Não pode participar da sessão!")
#     case '14': 
#       os.system('clear')
#       print("Você está livre para assistir o filme" if idade >= 14 else "Não pode participar da sessão!")
#     case '16': 
#       os.system('clear')
#       print("Você está livre para assistir o filme" if idade >= 16 else "Não pode participar da sessão!")
#     case '18': 
#       os.system('clear')
#       print("Você está livre para assistir o filme" if idade >= 18 else "Não pode participar da sessão!")

os.system('clear')

if classificacao == 'L':
    print('Você está livre para assistir!!')
elif classificacao.isdigit():
    idade_minima = int(classificacao)
    print("Você está livre para assistir o filme" if idade >= idade_minima else "Não pode participar da sessão!")
else:
    print('Classificação inválida')