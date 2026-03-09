import math

PI = 3.14159

raio = float(input('Qual é o raio do circulo? '))

def calcular_area_circulo(raio):
  return math.pi * raio ** 2

print(f'A área do círculo é {calcular_area_circulo(raio):.2f}')