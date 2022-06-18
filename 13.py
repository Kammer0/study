# study

class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):   
    velocidad = 0
    cilindrada = 0

    def Descripcion(self, velocidad, cilindrada):
        self.velocidad = velocidad
        self.cilindrada = cilindrada 
        print (f"Color del coche: {self.color}\nRuedas: {self.ruedas}\nPuertas: {self.puertas}\n\nVelocidad: {self.velocidad}\nCilindrada: {self.cilindrada}")
        

miCoche = Coche("Negro", 4, 5)

print (miCoche.Descripcion(110, 250))

 
