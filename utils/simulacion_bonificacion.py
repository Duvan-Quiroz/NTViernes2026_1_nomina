import random

def generar_bonificacion(numeroBonificacion):

    valoresBonificacion = [100, 200, 300, 400, 500]

    bonificaciones = []

    for i in range(numeroBonificacion):

        bonificacion = {
             #Valores correspondientes a cada bonificacion 
             "id" : random.randint(0, 100),
             "valor" : random.choice(valoresBonificacion),
        }

        bonificaciones.append(bonificacion)
    return bonificaciones