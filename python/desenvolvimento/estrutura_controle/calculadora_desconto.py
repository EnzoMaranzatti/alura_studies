# Faça uma calculadora de desconto. O usuário digita o valor da compra e o sistema aplica:
# 5% de desconto para compras acima de R$100, 10% acima de R$200 e 15% acima de R$500.

def calcular_desconto(valor, percentual):
    valor_desconto = valor * percentual
    valor_final = valor - valor_desconto
    return valor_final, valor_desconto

valor_compra = float(input('Digite o valor da sua compra: '))

percentual = 0
if 100 < valor_compra <= 200:
    percentual = 0.05
elif 200 < valor_compra <= 500:
    percentual = 0.10
elif valor_compra > 500:
    percentual = 0.15

if percentual > 0:
    valor_final, valor_desconto = calcular_desconto(valor_compra, percentual)
    print(f'Valor da compra: {valor_compra:.2f} | Desconto: {valor_desconto:.2f} | Total: {valor_final:.2f}')
else:
    print(f'Valor da compra: {valor_compra:.2f} | Sem desconto')
