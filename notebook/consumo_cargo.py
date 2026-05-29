import requests


def consumo_cargo():
    url = "http://localhost:8080/api/cargos"
    peticion = requests.get(url)
    peticion.raise_for_status()
    cargos = peticion.json()
    return cargos
