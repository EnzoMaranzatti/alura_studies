'''

Carlos trabalha em um cartório e precisa validar se um CPF informado pelo cliente tem o formato correto
antes de prosseguir com o atendimento. O CPF deve conter exatamente 11 dígitos numéricos. Se a entrada 
contiver letras ou qualquer outro caractere que não seja um número, o programa deve exibir uma mensagem de erro.

Crie um programa que peça ao usuário um número de CPF e verifique se ele tem 11 dígitos e contém apenas números.

'''

isvalid = False

while not isvalid:
   cpf = input('Digite seu cpf sem caracteres especiais: ')

   if cpf.isdigit() and len(cpf) == 11:
      isvalid = True
      print('CPF válido!')
      cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
      print(f'CPF formatado: {cpf_formatado}')
   else:
      print("CPF inválido! Digite exatamente 11 números.")