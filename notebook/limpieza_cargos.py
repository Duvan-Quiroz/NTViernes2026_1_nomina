import pandas as pd

def limpiar_datos_empleado(data_frame):
    data_frame_limpio=data_frame.copy()

    datos_texto=["nombre", "descripcion"]
    for columna in datos_texto:
        data_frame_limpio[columna]=data_frame_limpio[columna].astype("string").str.strip()

    #3convertir columnas numericas
    data_frame_limpio["id"]=pd.to_numeric(data_frame_limpio["id"])
    
    #4eliminar filas que traen datos obligatorios vacios
    columnas_obligatorias=["id", "nombre", "descripcion"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

    #5 Eliminar datos invalidos
    data_frame_limpio=data_frame_limpio[data_frame_limpio["id"]>0]
    data_frame_limpio=data_frame_limpio[data_frame_limpio["nombre"]>0]
    data_frame_limpio=data_frame_limpio[data_frame_limpio["descripcion"]>0]

    #6 Eliminar duplicados
    data_frame_limpio=data_frame_limpio.drop_duplicates()

    #7 Eliminar filas con datos obligatorios vacios
    columnas_obligatorias=["id","nombre","descripcion"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)
    return data_frame_limpio