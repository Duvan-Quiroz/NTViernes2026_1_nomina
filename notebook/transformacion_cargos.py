import pandas as pd


def transformar_cargos(data_frame_limpio):

    # Transformación 1 (cargos por nombre)
    filtro1 = data_frame_limpio
    agrupacion1 = filtro1.groupby("nombre")["id"].count().reset_index(name="cantidad_cargos")

    # Transformación 2 (cargos por descripción)
    filtro2 = data_frame_limpio
    agrupacion2 = filtro2.groupby("descripcion")["id"].count().reset_index(name="cantidad_por_descripcion")

    # Transformación 3 (cargos con descripciones repetidas)
    filtro3 = data_frame_limpio
    agrupacion3 = filtro3.groupby(["nombre", "descripcion"])["id"].count().reset_index(name="cantidad_repetidos")

    # Transformación 4 (descripciones únicas de cargos)
    filtro4 = data_frame_limpio.drop_duplicates(subset=["descripcion"])
    agrupacion4 = filtro4["descripcion"].reset_index(drop=True).rename("descripcion_unica").to_frame()

    # Transformación 5 (cargos por nombre y descripción)
    filtro5 = data_frame_limpio
    agrupacion5 = filtro5.groupby("nombre")["descripcion"].nunique().reset_index(name="descripciones_distintas")

    return {
        "cargos_por_nombre": agrupacion1,
        "cargos_por_descripcion": agrupacion2,
        "cargos_repetidos": agrupacion3,
        "descripciones_unicas": agrupacion4,
        "descripciones_por_nombre": agrupacion5
    }
