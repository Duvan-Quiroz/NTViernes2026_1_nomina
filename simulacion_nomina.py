import random
from datetime import datetime, timedelta

def generar_nomina(numeroEmpleado):

    empleados = []

    salarios = [1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]

    fechaNomina = datetime(2020, 1, 1)

    for i in range(numeroEmpleado):

        fecha = fechaNomina + timedelta(days=random.randint(0, 365))

        empleado = {
             #Valores correspondientes a cada empleado 
             "id" : random.randint(0, 100),
             "fecha" : fecha.strftime("%Y-%m-%d"),
             "salarioBase" : random.choice(salarios),
        }

        empleados.append(empleado)
    return empleados
       



       