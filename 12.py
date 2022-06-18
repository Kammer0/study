# study

def Bisiesto():
    num = int(input("Año: "))
    if num %4 == 0:
        print(f"El año {num} es bisiesto")
    elif num == 4 or num %4 != 0:
        print(f"El año {num} no es bisiesto")

print (Bisiesto())
        
