# Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. 
# Utilize um bloco try-except para lidar com possíveis exceções.

numero = [2, 3, 4, 5, 10, 230, 12, 11, 606, 'a']
soma = 0
try:
    for num in numero:
        soma += num
except TypeError:
    print(f'Valor inválido ignorado!')

print(soma)