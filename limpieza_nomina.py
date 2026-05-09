import pandas as pd
def limpiar_datos_nomina(data_frame_sucio):
    data_frame_limpio=data_frame_sucio.copy()

    #1 Limpiar espacios en blanco en las columnas de texto
    datos_texto=["periodo", "tipo_pago"]
    for columna in datos_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].str.strip()

    #2 Eliminar filas con valores nulos en columnas críticas
    columnas_criticas=["id_empleado", "fecha_pago", "salario_base"] 
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_criticas)
    
    
    #3 Convertir tipos de datos
    data_frame_limpio["id_empleado"] = data_frame_limpio["id_empleado"].astype(int)
    data_frame_limpio["fecha_pago"] = pd.to_datetime(data_frame_limpio["fecha_pago"], errors='coerce')
    data_frame_limpio["salario_base"] = pd.to_numeric(data_frame_limpio["salario_base"], errors='coerce')
    
    
    #4 Eliminar filas con fechas inválidas o salarios no numéricos  
    data_frame_limpio = data_frame_limpio.dropna(subset=["fecha_pago", "salario_base"])

    
    return data_frame_limpio

    