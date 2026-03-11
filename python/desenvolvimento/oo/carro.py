'''
Implemente uma classe chamada Carro com os atributos básicos,
como modelo, cor e ano. Crie uma instância dessa classe e 
atribua valores aos seus atributos.
'''

class Carro:
   carros = []
   def __init__(self, modelo, cor, ano):
      self.modelo = modelo
      self.cor = cor
      self.ano = ano
      Carro.carros.append(self)
   
   def listar_carros():
      print(f'{"Modelo".ljust(32)} {"Cor".ljust(24)} {"Ano"}')
      for carro in Carro.carros:
         print(f'{carro.modelo.ljust(32)} {carro.cor.ljust(24)} {carro.ano}')

porche = Carro('Porch Esportiva', 'Preto', 2025)
civic = Carro('Civic', 'Prateada', 2022)
focus = Carro('Focus', 'Preto', 2013)

Carro.listar_carros()

