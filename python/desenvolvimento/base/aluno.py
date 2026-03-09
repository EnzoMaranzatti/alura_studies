aluno = input('Nome do aluno: ')
notaI, notaS, notaTrabalho = float(input('Nota intermediaria: ')), float(input('Nota semestral: ')), float(input('Nota trabalho: '))
media = ((notaI + notaS) / 2) * 0.7 + notaTrabalho * 0.3

if media >= 7:
  print(f'Aluno {aluno} aprovado!! Media final {media}')
elif media >= 5 and media < 7:
  print(f'Aluno {aluno} recuperação. Media final {media}')
elif media < 5:
  print(f'Aluno {aluno} reprovado!! Media final {media}')
else:
  print('Erro...')