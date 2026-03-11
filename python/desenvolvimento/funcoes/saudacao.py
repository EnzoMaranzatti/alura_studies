'''
Beatriz está desenvolvendo um sistema de atendimento para um site de serviços. Ela deseja criar um programa que
exiba uma saudação personalizada dependendo da hora do dia que o usuário acessa a plataforma. 
O sistema deverá ter a seguinte regra:

- Se for antes das 12h, exibir "Bom dia";
- Entre 12h e 18h, exibir "Boa tarde";
- Após 18h, exibir "Boa noite".
'''

def saudacao_personalizada():
   mensagem = ''
   nome = input('Digite seu nome: ')
   horario = int(input('Digite o horario atual (No formatado de 24h): '))

   if horario <= 12:
      mensagem = f'Bom dia! Seja bem-vindo {nome}'
      print(mensagem)
   elif 12 < horario <= 18:
      mensagem = f'Boa tarde! Seja bem-vindo {nome}'
      print(mensagem)
   else:
      mensagem = f'Boa noite! Seja bem-vindo {nome}'
      print(mensagem)

saudacao_personalizada()