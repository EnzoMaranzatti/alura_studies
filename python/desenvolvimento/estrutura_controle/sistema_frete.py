cep = input('Digite seu cep: ')
peso_pacote = float(input('Qual o peso do pacote (kg): '))

def regiao(cep):
    regiao = ''
    if cep[0] == '1' or cep[0] == '2' or cep[0] == '3':
        regiao == 'SP'
    elif cep[0] == '4' or cep[0] == '5':
        regiao == 'Sul'
    elif cep[0] == '6' or cep[0] == '7':
        regiao == 'Nordeste'
    elif cep[0] == '8' or cep[0] == '9':
        regiao == 'Norte/Centro-Oeste'
    else:
        regiao == ''
    return regiao

localizacao = regiao(cep)

def calcular_frete(localizacao, peso_pacote):
    valor_frete = 0
    if localizacao == 'SP' and 1 < peso_pacote <= 2:
        valor_frete == 36
    elif localizacao == 'SP' and 1 < peso_pacote <= 2
        

