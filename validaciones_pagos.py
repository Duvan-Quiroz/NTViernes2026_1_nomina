def es_pago_valido(pago):
    
    if pago["id_pago"] <= 0:
        return False
    
    if pago["id_empleado"] is None or pago["id_empleado"] <= 0:
        return False
    
    if pago["valor"] <= 0:
        return False

    return True