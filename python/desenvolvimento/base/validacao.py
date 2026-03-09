nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
email = input("Digite seu email: ")

erros = []

# Validação do nome
if len(nome.strip()) < 3:
    erros.append("Nome inválido (mínimo 3 caracteres).")

# Validação da idade
if not idade.isdigit() or int(idade) <= 0:
    erros.append("Idade inválida (deve ser número positivo).")

# Validação do email
if "@" not in email:
    erros.append("Email inválido (deve conter '@').")

# Resultado final
if len(erros) == 0:
    print("\n✅ Dados válidos!")
    print(f"Nome: {nome.strip().title()}")
    print(f"Idade: {int(idade)} anos")
    print(f"Email: {email.strip().lower()}")
else:
    print("\n❌ Erros encontrados:")
    for erro in erros:
        print("-", erro)
