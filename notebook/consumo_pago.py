import requests


def consumo_pago():
    url = "http://localhost:8080/api/pagos"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    pagos = respuesta.json()
    return pagos