# Peça ao usuário um número e calcule o **fatorial** dele. Exemplo: 5! = 5 × 4 × 3 × 2 × 1 = 120

numero = int(input("Digite um número: "))

fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i  # fatorial = fatorial * i

print(f"{numero}! = {fatorial}")