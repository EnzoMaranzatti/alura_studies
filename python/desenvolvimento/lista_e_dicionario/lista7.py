# Construa um código que calcule a média dos valores em uma lista. 
# Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

numeros = [20, 10, 312, 102, 11, 43]

try:
    soma = 0
    for num in numeros:
        soma += num
    media = soma / len(numeros)
    print(f'Média: {media}')
except ZeroDivisionError:
    print('Não é possivel dividir por 0')