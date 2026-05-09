import pandas as pd

def limpieza_bonificacion(data_frame ):
    data_frame_limpio = data_frame.copy()

    data_frame_limpio['id'] = pd.to_numeric(data_frame_limpio['id'])
    data_frame_limpio['valor'] = pd.to_numeric(data_frame_limpio['valor'])

    columnas_obligatorias = ['id', 'valor']
    data_frame_limpio = data_frame_limpio.dropna(subset = columnas_obligatorias) 

    data_frame_limpio = data_frame_limpio [data_frame_limpio['id']>0]
    data_frame_limpio = data_frame_limpio [data_frame_limpio['valor']>0]

    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio