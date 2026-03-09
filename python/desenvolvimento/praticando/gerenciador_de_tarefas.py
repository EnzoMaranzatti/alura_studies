'''
Ana precisa de um programa simples para gerenciar suas tarefas diárias. Ela quer poder adicionar, 
visualizar e remover tarefas de uma lista.

Crie um programa com um menu interativo que permita ao usuário adicionar, visualizar e remover tarefas.
 Use uma lista para armazenar as tarefas.
'''

'''
TAREFA:
   - ID
   - titulo
   - estado (concluido, em andamento, pendente)
'''
import os

tarefas = []

def limpar_tela():
   os.system('clear')

def title(titulo):
   limpar_tela()
   print('-' * len(titulo))
   print(titulo)
   print('-' * len(titulo))

def menu():
   limpar_tela()
   print('''
888b     d888                           
8888b   d8888                           
88888b.d88888                           
888Y88888P888  .d88b.  88888b.  888  888
888 Y888P 888 d8P  Y8b 888 "88b 888  888
888  Y8P  888 88888888 888  888 888  888
888   "   888 Y8b.     888  888 Y88b 888
888       888  "Y8888  888  888  "Y88888         
''')
   print('\nGerenciador de Tarefas\n')
   print('1. Adicionar tarefa\n2. Visualizar tarefas\n3. Remover tarefas\n4. Sair')

def adicionar_tarefa():
   title('Adicionar tarefa')
   id_tarefa = len(tarefas) + 1
   estado_valido = ('concluído', 'concluido', 'em andamento', 'pendente')
   estado_correto = False
   titulo = input('Digite o titulo da tarefa: ')
   while not estado_correto:
      estado = input('Digite o estado da tarefa (concluido, em andamento ou pendente): ').lower()
      if estado in estado_valido:
         estado_correto = True
         break
   input('\nDigite uma tecla para voltar ao menu ')
   return titulo, estado, id_tarefa

def visualizar_tarefa():
   title('Visualizar Tarefa')
   if not tarefas:
      print('Nenhuma tarefa registrada!!')
      return 
   
   print(f'{"ID".ljust(8)} | {"Titulo".ljust(32)} | {"Estado"}')
   for tarefa in tarefas:
      print(f'{str(tarefa["ID"]).ljust(8)}   {tarefa["titulo"].ljust(32)}   {tarefa["estado"]}')
   
   input('\nDigite uma tecla para voltar ao menu ')

def deletar_tarefa():
   title('Deletar tarefa')
   if not tarefas:
      print('Nenhuma tarefa registrada!!')
      return 
   
   # mostra as tarefas para o usuário saber os IDs
   print(f'{"ID".ljust(8)} | {"Titulo".ljust(32)} | {"Estado"}')
   for tarefa in tarefas:
      print(f'{str(tarefa["ID"]).ljust(8)}   {tarefa["titulo"].ljust(32)}   {tarefa["estado"]}')

   while True:
      try:
         id_deletar = int(input('\nDigite o ID da tarefa que deseja deletar: '))

         for tarefa in tarefas:
            if tarefa['ID'] == id_deletar:
               tarefas.remove(tarefa)
               print(f'Tarefa "{tarefa["titulo"]}" removida com sucesso!')
               input('\nDigite uma tecla para voltar ao menu ')
               return
         
         print('ID não encontrado')
      except ValueError:
         print('Digite um número!!')


opcao = 0
while opcao != 4:
   menu()
   try:
      opcao = int(input('Digite uma opção: '))

      match opcao:
         case 1: 
            titulo_tarefa, estado_tarefa, id_tarefa = adicionar_tarefa()
            dados_tarefa = {'ID': id_tarefa, 'titulo': titulo_tarefa, 'estado': estado_tarefa}
            tarefas.append(dados_tarefa)
            limpar_tela()
            print('Tarefa adicionada com sucesso!!')
         case 2:
            visualizar_tarefa()
         case 3:
            deletar_tarefa()
         case 4: 
            print('\n\nSaindo...')
   except ValueError:
      print('Digite um número!!')