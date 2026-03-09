# Faça um verificador de ano bissexto. Um ano é bissexto se: 
# for divisível por 4, exceto anos divisíveis por 100, a menos que também sejam divisíveis por 400.

ano = int(input('Digite o ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')
