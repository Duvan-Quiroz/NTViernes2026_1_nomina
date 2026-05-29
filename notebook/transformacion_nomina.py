import pandas as pd

def transformar_datos_nomina(data_frame_limpio):
    # Transformación 1: cantidad de nóminas por empleado
    filtro1 = data_frame_limpio
    agrupacion1 = filtro1.groupby("id_empleado")["id_nomina"].count().reset_index(name="cantidad_nominas")

    # Transformación 2: salario total pagado por empleado
    filtro2 = data_frame_limpio
    agrupacion2 = filtro2.groupby("id_empleado")["total_pago"].sum().reset_index(name="salario_total_pagado")

    # Transformación 3: nóminas con pago alto >5000
    filtro3 = data_frame_limpio.query("total_pago > 5000")
    agrupacion3 = filtro3.groupby("id_empleado")["id_nomina"].count().reset_index(name="cantidad_nominas_pago_alto")

    # Transformación 4: rangos de pago
    filtro4 = data_frame_limpio.copy()
    filtro4["rango_pago"] = pd.cut(
        filtro4["total_pago"],
        bins=[0, 3000, 6000, 10000],
        labels=["Bajo", "Medio", "Alto"]
    )
    agrupacion4 = filtro4.groupby("rango_pago")["id_nomina"].count().reset_index(name="cantidad")

    # Transformación 5: nóminas por mes
    filtro5 = data_frame_limpio
    agrupacion5 = filtro5.groupby("mes")["id_nomina"].count().reset_index(name="cantidad_nominas_mes")

    return {
        "nominas_por_empleado": agrupacion1,
        "salario_total_pagado": agrupacion2,
        "nominas_pago_alto": agrupacion3,
        "rangos_pago": agrupacion4,
        "nominas_por_mes": agrupacion5
    }
