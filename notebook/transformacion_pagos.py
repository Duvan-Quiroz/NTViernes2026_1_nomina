import pandas as pd

def transformar_datos(data_frame_limpio):

    # Transformación 1 (pagos por método)
    filtro1 = data_frame_limpio
    agrupacion1 = filtro1.groupby("metodo")["id_pago"].count().reset_index(name="cantidad_pagos")

    # Transformación 2 (valor promedio por método)
    filtro2 = data_frame_limpio
    agrupacion2 = filtro2.groupby("metodo")["valor"].mean().reset_index(name="valor_promedio")

    # Transformación 3 (pagos con valor alto >3000)
    filtro3 = data_frame_limpio.query("valor > 3000")
    agrupacion3 = filtro3.groupby("metodo")["id_pago"].count().reset_index(name="cantidad_valor_alto")

    # Transformación 4 (rangos de valor)
    filtro4 = data_frame_limpio.copy()
    filtro4["rango_valor"] = pd.cut(
        filtro4["valor"],
        bins=[0, 2000, 5000, 10000],
        labels=["Bajo", "Medio", "Alto"]
    )
    agrupacion4 = filtro4.groupby("rango_valor")["id_pago"]\
        .count().reset_index(name="cantidad")

    # Transformación 5 (pagos por empleado)
    filtro5 = data_frame_limpio
    agrupacion5 = filtro5.groupby("id_empleado")["valor"]\
        .sum().reset_index(name="total_pagado")

    return {
        "pagos_metodo": agrupacion1,
        "promedio_valor": agrupacion2,
        "valor_alto": agrupacion3,
        "rangos_valor": agrupacion4,
        "pagos_empleado": agrupacion5
    }