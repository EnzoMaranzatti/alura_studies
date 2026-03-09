# Crie um dicionário e verifique se uma chave 
# específica existe dentro desse dicionário.

alunos = [
  {
    'nome': 'Enzo Vinicius Maranzatti da Silva',
    'idade': 20,
    'ra': '20235553',
    'cpf': '502.044.258-59'
  },
  {
    'nome': 'Eduardo Henrique',
    'idade': 24,
    'ra': '20235505',
    'cpf': '200.233.111-00'
  }
]

# Crie um dicionário e verifique se uma chave 
# específica existe dentro desse dicionário.

alunos = [
  {
    'nome': 'Enzo Vinicius Maranzatti da Silva',
    'idade': 20,
    'ra': '20235553',
    'cpf': '502.044.258-59'
  },
  {
    'nome': 'Eduardo Henrique',
    'idade': 24,
    'ra': '20235505',
    'cpf': '200.233.111-00'
  }
]

encontrado = False

def pesquisar_aluno():
   nome_aluno = input('Qual o nome do aluno: ').strip().lower()

   for aluno in alunos:
      if nome_aluno == aluno['nome'].lower():
         print('Aluno encontrado')
         encontrado = True
         break

   if not encontrado:
      print('Aluno não encontrado')

pesquisar_aluno()

