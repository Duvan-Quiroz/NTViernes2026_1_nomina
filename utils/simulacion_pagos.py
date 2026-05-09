import random


def generar_pagonomina(pagoNomina):
    metodos = ["efectivo", "transferencia", "tarjeta", "deposito"]
    valores = ["1000", "50000", "3000", "8000", "0", "-500", "2500"]
    nominas = []

    for i in range(pagoNomina):
        pago = {
            "id_pago": random.randint(1, 1000),
            "id_empleado": random.randint(1, 100),
            "valor": random.choice(valores),
            "metodo": random.choice(metodos)
        }

        probabilidad_error = random.random()

        if probabilidad_error < 0.1:
            pago["metodo"] = " " + pago["metodo"].upper()
        elif probabilidad_error < 0.2:
            pago["valor"] = random.choice(["-1000", "0", "no disponible"])
        elif probabilidad_error < 0.3:
            pago["id_pago"] = random.choice([-1, 0, None])
        elif probabilidad_error < 0.4:
            pago["id_empleado"] = random.choice([-5, 0, None])
        elif probabilidad_error < 0.5:
            pago["metodo"] = random.choice([None, "", "   "])

        nominas.append(pago)

    return nominas