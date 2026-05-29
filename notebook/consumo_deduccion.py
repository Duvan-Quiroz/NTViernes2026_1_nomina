import requests

def consumo_deduccion():
    url = "http://localhost:8080/api/deducciones"
    peticion = requests.get(url)
    peticion.raise_for_status()
    deducciones = peticion.json()
    return deducciones