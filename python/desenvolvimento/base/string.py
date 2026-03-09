nome = input('Digite seu nome: ')

print(f"Maiúsculas: {nome.upper()}")
print(f"Minúsculas: {nome.lower()}")
print(f"Primeira letra maiúscula: {nome.capitalize()}")
print(f"Título: {nome.title()}")
print(f"Quantidade de caracteres com espaço: {len(nome)}")
print(f"Quantidade de caracteres sem espaço: {len(nome.replace(' ', ''))}")

quantidade = nome.lower().count('a')

print(f"A letra 'a' aparece {quantidade} vezes.")
