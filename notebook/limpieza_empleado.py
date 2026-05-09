import pandas as pd

def limpiar_datos_empleado(data_frame):
    data_frame_limpio=data_frame.copy()

    #1 Limpiar espacios en blanco en las columnas de texto
    datos_texto=["nombre", "documento"]
    for columna in datos_texto:
        data_frame_limpio[columna]=data_frame_limpio[columna].astype("string").str.strip()

    #2 Definir valores esperados   
    nombres_validos=["Luis Perez", "Laura Rojas", "Jhon Cuesta", "Camilo Vega", "Alejandro Castrillon"]
    data_frame_limpio["nombre"]=data_frame_limpio["nombre"].where(data_frame_limpio["nombre"].isin(nombres_validos), pd.NA)

    #3convertir columnas numericas
    data_frame_limpio["id"]=pd.to_numeric(data_frame_limpio["id"])
    data_frame_limpio["salario"]=pd.to_numeric(data_frame_limpio["salario"])

    #4eliminar filas que traen datos obligatorios vacios
    columnas_obligatorias=["id", "nombre", "documento", "salario"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

    #5 Eliminar datos invalidos
    data_frame_limpio=data_frame_limpio[data_frame_limpio["id"]>0]
    data_frame_limpio=data_frame_limpio[data_frame_limpio["salario"]>0]

    #6 Eliminar duplicados
    data_frame_limpio=data_frame_limpio.drop_duplicates()

    #7 Eliminar filas con datos obligatorios vacios
    columnas_obligatorias=["id","nombre","documento","salario"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)
    return data_frame_limpio