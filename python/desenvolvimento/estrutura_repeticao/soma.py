# Peça 5 números ao usuário (use um loop) e mostre a **soma** de todos eles.

soma = 0

for i in range(5):
    num = int(input('Digite um numero: '))
    soma += num  # soma = soma + num

print(f"Soma: {soma}")
