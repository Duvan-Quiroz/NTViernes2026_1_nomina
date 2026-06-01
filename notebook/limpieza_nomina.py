import pandas as pd

def limpiar_datos_nomina(data_frame_sucio):
    # Hacemos una copia para no modificar los datos originales por accidente
    data_frame_limpio = data_frame_sucio.copy()

    # --- 1. Eliminar filas con valores nulos en columnas críticas ---
    # En tu simulación, el 10% de los datos genera 'salarioBase' como None
    columnas_criticas = ["id", "fecha", "salarioBase"] 
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_criticas)
    
    # --- 2. Convertir tipos de datos y capturar errores ---
    # Convertimos el ID a entero
    data_frame_limpio["id"] = data_frame_limpio["id"].astype(int)
    
    # errors='coerce' transformará la fecha inválida "2020-13-01" en un valor Nat (Not a Time/Nulo)
    data_frame_limpio["fecha"] = pd.to_datetime(data_frame_limpio["fecha"], errors='coerce')
    
    # Convertimos el salario a numérico por si acaso
    data_frame_limpio["salarioBase"] = pd.to_numeric(data_frame_limpio["salarioBase"], errors='coerce')
    
    # --- 3. Eliminar los registros dañados por la conversión ---
    # Aquí borramos las filas donde la fecha se rompió ("2020-13-01") o el salario no sea un número
    data_frame_limpio = data_frame_limpio.dropna(subset=["fecha", "salarioBase"])

    # --- 4. Limpieza lógica de IDs de la simulación ---
    # Tu simulación inyecta IDs como -1, -24 o 0. Un ID válido debe ser mayor a 0.
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]
    
    return data_frame_limpio