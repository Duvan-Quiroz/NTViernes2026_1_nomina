import pandas as pd

def limpiar_datos_deduccion(data_frame):
    data_frame_limpio = data_frame.copy()

    # 1 Convertir columnas numéricas
    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"], errors="coerce")
    data_frame_limpio["valor"] = pd.to_numeric(data_frame_limpio["valor"], errors="coerce")

    # 2 Eliminar filas con datos obligatorios vacíos
    columnas_obligatorias = ["id", "valor"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    # 3 Eliminar datos inválidos
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["valor"] > 0]

    # 4 Eliminar duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    # 5 Verificación final de nulos en columnas obligatorias
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    return data_frame_limpio