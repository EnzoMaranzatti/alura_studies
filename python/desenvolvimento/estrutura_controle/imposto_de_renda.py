# Crie um programa que leia o salário de um funcionário e calcule o imposto de renda: 
# isento até R$2.500, 7,5% de R$2.501 a R$3.500, 15% de R$3.501 a R$4.500 e 22,5% acima de R$4.500.

salario = float(input('Digite seu salario: '))
imposto = 0

if 2500 < salario <= 3500:
    imposto = 0.075
elif 3500 < salario <= 4500:
    imposto = 0.15
elif salario > 4500:
    imposto = 0.225

def calcular_imposto(salario, imposto):
    valor_imposto = salario * imposto
    valor_final = salario - valor_imposto
    return valor_imposto, valor_final

if imposto > 0:
    valor_imposto, valor_final = calcular_imposto(salario, imposto)
    print(f'Salario: {salario:.2f} | Imposto: {valor_imposto:.2f} | Total: {valor_final:.2f}')
else:
    print(f'Salario: {salario:.2f} | Imposto: Isento')