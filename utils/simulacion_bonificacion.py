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

        probabilidadError = random.random()

        if probabilidadError < 0.1:
            bonificacion["id"] = random.choice([-1, -24, 0])
        elif probabilidadError < 0.2:
           bonificacion["valor"] = random.choice([-1000, -500, 0])   
          
        bonificaciones.append(bonificacion)
    return bonificaciones