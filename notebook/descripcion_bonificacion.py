import pandas as pd

def descripcion_bonificacion(data_frame_limpio):

    print("*** DESCRIPCION DEL DATASET ***")
    print(f"Número de filas del dataset: {data_frame_limpio.shape[0]}")
    print(f"Número de columnas del dataset: {data_frame_limpio.shape[1]}")
    print(f"Lista de columnas disponibles: {list(data_frame_limpio.columns)}")
    print(f"Tipos de dato de cad aatributo: {data_frame_limpio.dytes}")


   #Estadisticas
def descripcion_estadisticas(data_frame_limpio):   
    print("***ESTADISTICAS***")
    print(f"{data_frame_limpio[["id","valor"]].describe()}")


    #Conteos
def descripcion_conteo(data_frame_limpio):    
    print("***CONTEOS***")
    print(f"{data_frame_limpio["id"].value_counts()}")
    print(f"{data_frame_limpio["valor"].value_counts()}")