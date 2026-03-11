'''
Crie uma classe chamada Restaurante com os atributos nome, 
categoria, ativo e crie mais 2 atributos. Instancie um 
restaurante e atribua valores aos seus atributos.
'''
import os 

class Restaurante:
   restaurantes = []
   def __init__(self, nome, categoria, localizacao, telefone):
      self.nome = nome
      self.categoria = categoria
      self.localizacao = localizacao
      self.telefone = telefone
      self.ativo = False
      Restaurante.restaurantes.append(self)
   
   def listar_restaurantes():
      os.system('clear')
      print(f'{"Nome".ljust(32)} {"Categoria".ljust(12)} {"Localizacao".ljust(40)} {"Telefone".ljust(18)} {"Ativo"}')
      for restaurante in Restaurante.restaurantes:
         print(f'{restaurante.nome.ljust(32)} {restaurante.categoria.ljust(12)} {restaurante.localizacao.ljust(40)} {restaurante.telefone.ljust(18)} {restaurante.ativo}')

   def __str__(self):
      return f'Imprimindo restaurante - {self.nome}'


restaurante_sp = Restaurante('Churrascaria SP', 'Carne', 'Bem Brasil', '17 99137-2203')
Restaurante.listar_restaurantes()
print(restaurante_sp)

