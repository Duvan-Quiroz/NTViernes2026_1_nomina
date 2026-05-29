import pandas as pd

def transformar_datos(data_frame_limpio):

    # Transformación 1 (conteo por id)
    filtro1 = data_frame_limpio
    agrupacion1 = filtro1.groupby("id")["valor"].count().reset_index(name="cantidad_deducciones")

    # Transformación 2 (valor promedio por id)
    filtro2 = data_frame_limpio
    agrupacion2 = filtro2.groupby("id")["valor"].mean().reset_index(name="valor_promedio")

    # Transformación 3 (deducciones con valor alto >30)
    filtro3 = data_frame_limpio.query("valor > 30")
    agrupacion3 = filtro3.groupby("id")["valor"].count().reset_index(name="cantidad_valor_alto")

    # Transformación 4 (rangos de valor)
    filtro4 = data_frame_limpio.copy()
    filtro4["rango_valor"] = pd.cut(
        filtro4["valor"],
        bins=[0, 20, 50, 100],
        labels=["Bajo", "Medio", "Alto"]
    )
    agrupacion4 = filtro4.groupby("rango_valor")["id"]\
        .count().reset_index(name="cantidad")

    # Transformación 5 (total deducido por id)
    filtro5 = data_frame_limpio
    agrupacion5 = filtro5.groupby("id")["valor"]\
        .sum().reset_index(name="total_deducido")

    return {
        "deducciones_id": agrupacion1,
        "promedio_valor": agrupacion2,
        "valor_alto": agrupacion3,
        "rangos_valor": agrupacion4,
        "total_deducido": agrupacion5
    }