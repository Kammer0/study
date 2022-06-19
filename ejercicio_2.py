# study
import pickle

class Vehiculo():
    marca = ""
    modelo = 0
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def __str__(self):
        return f"Mi coche {self.marca} es del año {self.modelo}"
        
miCoche = Vehiculo("BMW", 2005)   
         


f = open ("vehiculo_data.bin", "wb")
pickle.dump(miCoche, f)
f.close()

f = open ("vehiculo_data.bin", "rb")
miCoche = pickle.load(f)

print(miCoche)
 
f.close()


 
