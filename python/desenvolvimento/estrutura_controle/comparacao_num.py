num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

if num1 > num2:
    print(f'{num1} é maior que o número {num2}')
elif num1 < num2:
    print(f'{num2} é maior que o número {num1}')
else:
    print(f'{num1} é igual a {num2}')