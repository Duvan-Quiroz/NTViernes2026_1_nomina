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

        #Inyectar errores controlados en nuestra base de datos
        probabilidadError = random.random()
        if probabilidadError < 0.1:  # 10% de probabilidad de error
            empleado["salarioBase"] = None  # Salario base faltante
        elif probabilidadError < 0.2:  # 10% de probabilidad de error
            empleado["fecha"] = "2020-13-01"  # Fecha inválida  
        elif probabilidadError < 0.3:
            empleado["id"] = random.choice([-1, -24, 0]) # ID inválido
        empleados.append(empleado)
    return empleados
       



       