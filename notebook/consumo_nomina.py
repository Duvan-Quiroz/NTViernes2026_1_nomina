import requests


def consumo_nomina():
	url = "http://localhost:8080/api/nominas"
	peticion = requests.get(url)
	peticion.raise_for_status()
	nominas = peticion.json()
	return nominas
