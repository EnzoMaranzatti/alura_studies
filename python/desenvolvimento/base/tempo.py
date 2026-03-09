isvalid = False

while not isvalid:
    segundos = input('Digite a quantidade em segundos: ')

    if segundos.isdigit():
        segundos = int(segundos)
        isvalid = True
        
        horas = segundos // 3600

        resto = segundos % 3600
        minutos = resto // 60
        segundos_finais = resto % 60
        print(f"{horas} hora(s), {minutos} minuto(s) e {segundos_finais} segundo(s)")



