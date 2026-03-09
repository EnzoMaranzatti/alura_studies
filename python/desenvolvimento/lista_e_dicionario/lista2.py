# Crie uma lista e utilize um loop for para percorrer todos os elementos da lista
alunos = [
  'Enzo Vinicius',
  'Diego Renata',
  'Maria Vitória',
  'Eduardo Henrique',
  'Henrique'
]

for indice, aluno in enumerate(alunos, start=1):
    print(indice, aluno)