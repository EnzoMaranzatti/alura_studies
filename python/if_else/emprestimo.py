'''
Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:

O valor da renda mensal precisa ser maior que R$ 2.000,00.
O valor da parcela não pode ultrapassar 30% da renda.
Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. 
O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima
'''

renda = float(input("Digite sua renda mensal: R$ "))
parcela = float(input("Digite o valor da parcela desejada: R$ "))

limite_parcela = renda * 0.30

if renda > 2000 and parcela <= limite_parcela:
    print("Empréstimo APROVADO ✅")
else:
    print("Empréstimo NEGADO ❌")


