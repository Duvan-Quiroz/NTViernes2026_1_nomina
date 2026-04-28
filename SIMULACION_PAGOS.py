import random
def generar_pagonomina(pagoNomina):
    listaValor= ["1000","50000","3000","8000"]
    nominas=[]
    for i in range(pagoNomina):
        nomina={
        "id":random.randint(0,1000),
        "valor":random.choice(listaValor)}
        nominas.append(nomina)
        return nominas