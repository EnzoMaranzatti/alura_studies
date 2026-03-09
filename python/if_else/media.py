''''
Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, 
ficaram de recuperação ou reprovados. As regras são:

Média >= 7: Aprovado
5 <= Média < 7: Recuperação
Média < 5: Reprovado
Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno.

'''

nome_aluno = input('Digite o nome do aluno: ')
nota_intermediaria = float(input('Digite a nota intermediaria: '))
nota_semestral = float(input('Digite a nota semestral: '))
nota_trabalho = float(input('Digite a nota do trabalho: '))

media = (nota_intermediaria + nota_semestral) / 2 * 0.7 + nota_trabalho * 0.3

if media >= 7:
   print(f'Aluno {nome_aluno} aprovado!! Sua média final é {media}')
elif 5 <= media < 7:
   print(f'Aluno {nome_aluno} ficou de exame! Sua média final é {media}')
else:
   print(f'Aluno {nome_aluno} reprovado! Sua média final é {media}')