from pagos.validaciones_pagos import es_pago_valido

def limpiar_pagos(pagos):
    pagos_limpios = []

    for pago in pagos:

        #1  Normalizar método
        pago["metodo"] = pago["metodo"].lower()

        #2 Corregir valores negativos
        if pago["valor"] < 0:
            pago["valor"] = abs(pago["valor"])

        #3 Validar
        if es_pago_valido(pago):
            pagos_limpios.append(pago)

    return pagos_limpios