import os

from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
class Restaurante:
   restaurantes = []

   # Metodo construtor: sempre que criar a instancia de um objeto o construtor vai ser chamado
   # self referencia da instancia atual
   def __init__(self, nome, categoria):
      self._nome = nome.title()
      self._categoria = categoria.upper()
      self._ativo = False
      self._avaliacao = []
      self._cardapio = []
      Restaurante.restaurantes.append(self)

   def __str__(self):
      return f'{self._nome} - {self._categoria}'

   @classmethod
   def listar_restaurantes(cls):
      print(f'{"Restaurante".ljust(32)} | {"Categoria".ljust(24)} | {"Avaliação".ljust(16)} | {"Estado"}')
      for restaurante in cls.restaurantes:
         print(f'{restaurante._nome.ljust(32)}   {restaurante._categoria.ljust(24)}   {str(restaurante.media_avaliacoes).ljust(16)}  {restaurante.ativo}')

   @property 
   def ativo(self):
      return '🟢' if self._ativo else '🔴' 
   
   def alternar_estado(self):
      self._ativo = not self._ativo

   def receber_avaliacao(self, cliente, nota):
      if 0 < nota <= 5:
         avaliacao = Avaliacao(cliente, nota)
         self._avaliacao.append(avaliacao)
   
   @property
   def media_avaliacoes(self):
      if not self._avaliacao:
         return '-'
      
      soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
      quantidade_de_notas = len(self._avaliacao)
      media = round(soma_das_notas / quantidade_de_notas, 1)
      return media

   '''  
      def adicionar_bebida_cardapio(self, bebida):
         self._cardapio.append(bebida)
      
      def adicionar_prato_cardapio(self, prato):
         self._cardapio.append(prato)
   '''
   def adicionar_cardapio(self, item):
      if isinstance(item, ItemCardapio):
         self._cardapio.append(item)

   # propery - Apenas leitura
   @property
   def exibir_cardapio(self):
      os.system('clear')
      print(f'Cardapio do restaurante {self._nome.upper()}\n')
      print(f'{"ID".ljust(10)} {"Nome".ljust(32)} {"Preço".ljust(16)}   {"Descrição/Tamanho".ljust(30)}\n')

      for i, item in enumerate(self._cardapio, start=1):
         if hasattr(item, 'descricao'):
            mensagem_prato = f'{str(i).ljust(10)} {item._nome.ljust(32)} R${str(item._preco).ljust(16)} {item.descricao.ljust(30)}\n'
            print(mensagem_prato)
         else:
            mensagem_bebida = f'{str(i).ljust(10)} {item._nome.ljust(32)} R${str(item._preco).ljust(16)} {item.tamanho.ljust(30)}\n'
            print(mensagem_bebida)