import requests


def consumo_bonificacion():
    url = "http://localhost:8080/api/bonificaciones"
    peticion = requests.get(url)
    peticion.raise_for_status()
    bonificaciones = peticion.json()
    return bonificaciones
