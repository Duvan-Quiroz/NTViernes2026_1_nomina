import random

def crear_empleados(nominaEmpleados):
    nombreEmpleados = ["Luis Perez", "Laura Rojas", "Jhon Cuesta", "Camilo Vega", "Alejandro Castrillon"]
    documentoEmpleados = ["123", "125", "145", "1000", "999"]

    empleados = []

    for i in range(nominaEmpleados):
        empleado = {
            "id": random.randint(1, 1000),
            "nombre": random.choice(nombreEmpleados),
            "documento": random.choice(documentoEmpleados),
            "salario": random.uniform(1000, 5000)
        }

        #inyectar errores controlados en nuestra base de datos
        probabilidadError = random.random()

        if probabilidadError < 0.1:
            empleado["nombre"] = " " + empleado["nombre"].lower()
        elif probabilidadError < 0.2:
            empleado["documento"] = " " + empleado["documento"] + " "
        elif probabilidadError < 0.3:
            empleado["id"] = random.choice([-1, -24, 0])
        elif probabilidadError < 0.4:
            empleado["salario"] = random.choice([-1000, -500, 0])    

        empleados.append(empleado)

    return empleados