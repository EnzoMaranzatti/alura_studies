isvalid = False

while not isvalid:
    cpf = input('Digite seu cpf sem caracteres especiais: ')
    
    if cpf.isdigit() and len(cpf) == 11:
        isvalid = True
        cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        print(f'CPF formatado: {cpf_formatado}')
    else:
        print("CPF inválido! Digite exatamente 11 números.")
