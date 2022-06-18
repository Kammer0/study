# study

class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        estado = "desaprobado"
    
        if self.nota >= 7:
            estado = "aprobado"
            
        return ("El alumno se llama {}, su nota es {}, por ende está {}".format(self.nombre, self.nota, estado))

a = Alumno("Santi", 6)

print(a)
