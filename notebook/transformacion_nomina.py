import pandas as pd

def transformar_datos_nomina(data_frame_limpio):
    # Aseguramos que la fecha sea tipo datetime para poder extraer el mes después
    data_frame_limpio["fecha"] = pd.to_datetime(data_frame_limpio["fecha"])

    # --- Transformación 1: cantidad de nóminas por empleado ---
    # Cambios: 'id_empleado' -> 'id' | 'id_nomina' -> 'id' (contamos sus registros)
    agrupacion1 = data_frame_limpio.groupby("id")["id"].count().reset_index(name="cantidad_nominas")

    # --- Transformación 2: salario total pagado por empleado ---
    # Cambios: 'id_empleado' -> 'id' | 'total_pago' -> 'salarioBase'
    agrupacion2 = data_frame_limpio.groupby("id")["salarioBase"].sum().reset_index(name="salario_total_pagado")

    # --- Transformación 3: nóminas con pago alto > 4000 ---
    # Cambios: 'total_pago' -> 'salarioBase'. Como el salario máximo simulado es 5000, 
    # bajé el filtro a > 4000 para que esta agrupación no te quede vacía.
    filtro3 = data_frame_limpio.query("salarioBase > 4000")
    agrupacion3 = filtro3.groupby("id")["id"].count().reset_index(name="cantidad_nominas_pago_alto")

    # --- Transformación 4: rangos de pago ---
    # Cambios: 'total_pago' -> 'salarioBase'. 
    # Adapté los 'bins' a los rangos de tu lista de salarios (1500 a 5000)
    filtro4 = data_frame_limpio.copy()
    filtro4["rango_pago"] = pd.cut(
        filtro4["salarioBase"],
        bins=[0, 2500, 4000, 6000],
        labels=["Bajo", "Medio", "Alto"]
    )
    agrupacion4 = filtro4.groupby("rango_pago", observed=False)["id"].count().reset_index(name="cantidad")

    # --- Transformación 5: nóminas por mes ---
    # Como la simulación no trae columna 'mes', creamos una temporal mapeando el nombre del mes
    filtro5 = data_frame_limpio.copy()
    filtro5["mes"] = filtro5["fecha"].dt.strftime('%B') # Extrae el nombre del mes (ej: January, February...)
    agrupacion5 = filtro5.groupby("mes")["id"].count().reset_index(name="cantidad_nominas_mes")

    return {
        "nominas_por_empleado": agrupacion1,
        "salario_total_pagado": agrupacion2,
        "nominas_pago_alto": agrupacion3,
        "rangos_pago": agrupacion4,
        "nominas_por_mes": agrupacion5
    }