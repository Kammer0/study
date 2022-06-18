# study

def NumeroPrimo():
    num = int(input("Ingrese su Numero: "))    
    if num > 1:
        for i in range(2, int(num)):
            if int(num) % i == 0:
                print (f"El numero -{num}- no es primo")
                break
            else:
                print(f"El numero -{num}- es primo")
                break
print(NumeroPrimo())
