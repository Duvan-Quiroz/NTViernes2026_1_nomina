import pandas as pd

def limpiar_datos_cargo(data_frame):
    data_frame_limpio = data_frame.copy()

    # 1 y 2. Limpiar espacios en blanco en las columnas de texto
    datos_texto = ["nombre", "descripcion"]
    for columna in datos_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip()

    # 3. Convertir columnas numéricas
    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"])
    
    # 4. Eliminar filas que traen datos obligatorios vacíos (Nulos/NaN)
    columnas_obligatorias = ["id", "nombre", "descripcion"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    # 5. Eliminar datos inválidos
    # Para el ID numérico, está perfecto buscar mayores a 0
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]
    
    # Para los textos, validamos que tengan caracteres (longitud mayor a 0)
    data_frame_limpio = data_frame_limpio[data_frame_limpio["nombre"].str.len() > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["descripcion"].str.len() > 0]

    # 6. Eliminar duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio