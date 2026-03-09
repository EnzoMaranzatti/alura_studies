# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

soma = 0

for i in range(1,51, 2):
    soma_anterior = soma
    soma += i
    print(f'{soma_anterior} + {i} = {soma}')
