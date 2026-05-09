import pandas as pd

def describir_empleados(data_frame_limpio):
    
    print("*** DESCRIPCION DEL DATASET ***")
    print(f"Número de filas del dataset: {data_frame_limpio.shape[0]}")
    print(f"Número de columnas del dataset: {data_frame_limpio.shape[1]}")
    print(f"Lista de columnas disponibles: {list(data_frame_limpio.columns)}")
    print(f"Tipos de dato de cad aatributo: {data_frame_limpio.dytes}")


   #Estadisticas
def describir_estadisticas(data_frame_limpio):   
    print("***ESTADISTICAS***")
    print(f"{data_frame_limpio[["id","salarioBase"]].describe()}")


    #Conteos
def describir_conteos(data_frame_limpio):    
    print("***CONTEOS***")
    print(f"{data_frame_limpio["id"].value_counts()}")
    print(f"{data_frame_limpio["salarioBase"].value_counts()}")
    
     
def describir_fechas(data_frame_limpio):
    print("\n***Rangos de fechas***")
    print(f"fecha minima: {data_frame_limpio['fecha'].min()}")
    print(f"fecha maxima: {data_frame_limpio['fecha'].max()}")
