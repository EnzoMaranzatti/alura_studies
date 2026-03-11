'''
Uma escola realizou um concurso de redação, e o próximo passo é organizar as notas dos participantes para definir a ordem 
de premiação. Para garantir transparência, as notas precisam ser classificadas em ordem crescente, do menor para o maior valor.

Com base nisso, desenvolva um programa que receba como entrada uma lista contendo as notas de todos os participantes e exiba, 
ao final, essa lista ordenada em ordem crescente.

Exemplo de Entrada:

Notas: [85, 70, 90, 60, 75]

Saída esperada:

Notas ordenadas: [60, 70, 75, 85, 90]
'''

notas = [85, 70, 90, 60, 75]

def ordem_crescente(notas):
   notas.sort()
   return notas

def ordem_decrecente(notas):
   # return sorted(notas, reverse=True)
   notas_crescente = ordem_crescente(notas)
   notas_descrescente = notas_crescente.reverse()
   return notas_crescente


print(f'{notas} qual ordem quer organizar? Crescente ou Decrescente\n')
op = input('Digite a ordem desejada: ').strip().lower()

if op == 'crescente':
   print(ordem_crescente(notas))
else:
   print(ordem_decrecente(notas))