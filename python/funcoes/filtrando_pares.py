'''
Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa filtrar apenas os valores pares de 
uma lista de números informada pelo usuário.

Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().
'''

def filtra_pares():
   numeros = input('Digite numeros inteiros separados por espaço: ').split()
   lista_numeros = [int(num) for num in numeros]

   for pares in lista_numeros:
      if pares % 2 == 0:
         print(pares)

filtra_pares()