'''
A professora Helena quer facilitar sua rotina na hora de calcular a média das notas finais da turma. 
Ela sempre anota as notas dos alunos ao longo do semestre e, no final, precisa de um relatório para 
saber se a turma está indo bem.

Para isso, ajude a professora a criar um programa que receba as notas finais de todos os alunos e 
calcule a média da turma.
'''

notas = input('Digite as notas dos alunos separados por virgula: ').strip()

lista_notas = [float(nota) for nota in notas.split(",")]
media = sum(lista_notas) / len(lista_notas)
print(f"Média da turma: {media:.2f}")