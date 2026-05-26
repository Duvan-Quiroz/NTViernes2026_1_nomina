
import pandas as pd

def transformar_datos(data_frame_limpio):

    # Transformación 1 (empleados por nombre)
    filtro1 = data_frame_limpio
    agrupacion1 = filtro1.groupby("nombre")["id"].count().reset_index(name="cantidad_empleados")


    # Transformación 2 (salario promedio por nombre)
    filtro2 = data_frame_limpio
    agrupacion2 = filtro2.groupby("nombre")["salario"].mean().reset_index(name="salario_promedio")


    # Transformación 3 (empleados con salario alto >3000)
    filtro3 = data_frame_limpio.query("salario > 3000")
    agrupacion3 = filtro3.groupby("nombre")["id"].count().reset_index(name="cantidad_salario_alto")


    # Transformación 4 (rangos salariales)
    filtro4 = data_frame_limpio.copy()

    filtro4["rango_salario"] = pd.cut(
        filtro4["salario"],
        bins=[0,2000,3500,5000],
        labels=["Bajo","Medio","Alto"]
    )

    agrupacion4 = filtro4.groupby("rango_salario")["id"]\
        .count().reset_index(name="cantidad")


    # Transformación 5 (documentos por tipo)
    filtro5 = data_frame_limpio
    agrupacion5 = filtro5.groupby("documento")["id"]\
        .count().reset_index(name="cantidad_documentos")


    return {
        "empleados_nombre":agrupacion1,
        "promedio_salario":agrupacion2,
        "salario_alto":agrupacion3,
        "rangos_salario":agrupacion4,
        "tipo_documento":agrupacion5
    }