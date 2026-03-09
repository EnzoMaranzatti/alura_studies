idade = int(input('Digite sua idade: '))

if idade <= 12:
    print(f'Criança - {idade}')
elif 13 <= idade <= 17:
    print(f'Adolecente - {idade}') 
else:
    print(f'Adulto - {idade}') 