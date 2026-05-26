import requests


def consumo_empleado():
    url = "http://localhost:8080/api/empleados"
    peticion = requests.get(url)
    peticion.raise_for_status()
    empleados = peticion.json()
    return empleados