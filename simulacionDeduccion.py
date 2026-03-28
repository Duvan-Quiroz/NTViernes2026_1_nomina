import random

def generar_deduccion(numero_deducciones):
    
    listaValor = [10, 20, 30, 40, 80]  # Ejemplo de valores posibles para las deducciones

    deducciones = []
    for _ in range(numero_deducciones):
        deduccion = {
            "id": random.randint(1, 100),
            "valor": random.choice(listaValor)
        }
        deducciones.append(deduccion)
    return deducciones