nome_completo = input("Digite seu nome completo: ").strip()

partes = nome_completo.split()

quantidade_palavras = len(partes)
primeiro_nome = partes[0]
ultimo_nome = partes[-1]
iniciais = ""

for parte in partes:
    iniciais += parte[0].upper()

print("\n--- Análise do Nome ---")
print(f"Quantidade de palavras: {quantidade_palavras}")
print(f"Primeiro nome: {primeiro_nome}")
print(f"Último nome: {ultimo_nome}")
print(f"Iniciais: {iniciais}")
