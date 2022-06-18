# study

from time import *


print("Hoy es",strftime("%d/%m/%Y"),"Y son las",strftime("%H:%M"))


def HoraFin():
    if int(strftime("%H")) >= 19:
        print("Son las {}:{}, es hora de irse a casa, tu turno finalizó a las 19:00".format(strftime("%H"), strftime("%M")))
        
    else:
        hour = 19 - int(strftime("%H"))
        min = 60 - int(strftime("%M"))
        print("Faltan {} horas y {} minutos para irse".format(hour, min))

print (HoraFin())

