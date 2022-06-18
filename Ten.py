# study


altura = int(input("Altura: "))
base =  int(input("Base: "))
    
def AreaTriangulo(x, y):
     return (x * y) / 2

print("El area del triangulo es:", AreaTriangulo(base, altura))


radio_circulo = int(input("Radio: "))

from math import pi

def AreaCirculo(x):
     return pi * x**2

print("El area del circulo es:",round(AreaCirculo(radio_circulo), 2))
