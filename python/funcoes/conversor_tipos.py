'''
Pedro está criando um sistema de cadastro de produtos para sua loja e percebeu que todos os números de telefone dos clientes
estão armazenados como strings. No entanto, para facilitar buscas e validações, ele precisa que esses números sejam tratados 
como inteiros.

Dado o seguinte código com uma lista de números de telefone armazenados incorretamente como str, faça duas funções, uma que 
converte os tipos para inteiro e outra que verifica se a conversão foi feita corretamente e todos os números de telefone são 
inteiros:


telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 
'''

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

def telefone_formatado(telefones):
   telefone_formatado = ''
   telefones_formatados = []
   for telefone in telefones:
      #                    (00) 00000-0000
      telefone_formatado = f'({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}'
      telefones_formatados.append(telefone_formatado)
   
   return telefones_formatados

def converter_telefone(telefones):
   telefones_int = []

   for telefone in telefones:
      telefones_int.append(int(telefone))

   return telefones_int

telefones_formatados = telefone_formatado(telefones)
telefones_int = converter_telefone(telefones)

print(f'{telefones} - Lista de String')
print(f'{telefones_formatados} - Lista Formatada')
print(f'{telefones_int} - Lista Inteiro')