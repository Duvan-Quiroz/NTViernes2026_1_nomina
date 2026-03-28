import random

def crear_empleados(nominaEmpleados):
    nombreEmpleados=["Luis Perez", "Laura Rojas", "Jhon Cuesta", "Camilo Vega", "Alejadro Castrillon"]
    documentoEmpleados=["123", "125", "145", "1000", "999"]

    empleados=[]
    for i in range(nominaEmpleados):
        empleado={
            "id":random.randint(0,1000),
            "nombre":random.choice(nombreEmpleados),
            "documento":random.choice(documentoEmpleados),
            "salario":random.uniform()
        }
        empleados.append(empleado)
        return empleados
