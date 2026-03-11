'''
Uma ONG está organizando uma campanha de arrecadação de alimentos e precisa registrar os nomes dos voluntários que 
vão ajudar na ação. À medida que os voluntários se inscrevem, seus nomes devem ser adicionados à lista e quando for 
digitado a palavra sair o programa deve encerrar.

Ajude a ONG a criar um programa que permita registrar os voluntários e exiba a lista completa no final.
'''
import os

voluntarios = []

def registrar_voluntario(nome):
   voluntarios.append(nome)

def listar_voluntarios():
   os.system('clear')
   for voluntario in voluntarios:
      print(voluntario)

nome_voluntario = ''
while nome_voluntario != 'sair':
   nome_voluntario = input("Digite o nome do voluntário (ou 'sair' para encerrar): ").lower()

   if nome_voluntario != 'sair':
      nome_voluntario.title()
      registrar_voluntario(nome_voluntario)
   
listar_voluntarios()
   
