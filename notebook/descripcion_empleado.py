import pandas as pd

def describir_empleados(data_frame_limpio):
    """Describe un DataFrame de empleados con estadísticas y conteos básicos."""

    if data_frame_limpio is None:
        print("No se recibió ningún DataFrame para describir.")
        return

    if isinstance(data_frame_limpio, list):
        data_frame_limpio = pd.DataFrame(data_frame_limpio)
    elif not isinstance(data_frame_limpio, pd.DataFrame):
        try:
            data_frame_limpio = pd.DataFrame(data_frame_limpio)
        except Exception as e:
            print(f"No se pudo convertir el input a DataFrame: {e}")
            return

    print("*** DESCRIPCION DEL DATASET ***")
    print(f"Número de filas del dataset: {data_frame_limpio.shape[0]}")
    print(f"Número de columnas del dataset: {data_frame_limpio.shape[1]}")
    print(f"Columnas disponibles: {list(data_frame_limpio.columns)}")
    print("Tipos de dato de cada atributo:")
    print(data_frame_limpio.dtypes)

    print("\n*** VALORES FALTANTES ***")
    faltantes = data_frame_limpio.isna().sum()
    print(faltantes[faltantes > 0] if faltantes.any() else "No hay valores faltantes.")

    print("\n*** ESTADÍSTICAS NUMÉRICAS ***")
    try:
        print(data_frame_limpio.select_dtypes(include=["number"]).describe())
    except Exception as e:
        print(f"No se pudieron calcular estadísticas numéricas: {e}")

    print("\n*** RESUMEN DE COLUMNAS CLAVE ***")
    columnas_clave = ["id", "nombre", "documento", "salario"]
    for columna in columnas_clave:
        if columna in data_frame_limpio.columns:
            print(f"\n-- {columna} --")
            if pd.api.types.is_numeric_dtype(data_frame_limpio[columna].dtype):
                print(data_frame_limpio[columna].describe())
            else:
                print(data_frame_limpio[columna].value_counts(dropna=False))
        else:
            print(f"La columna '{columna}' no está presente en el dataset.")

    if "salario" in data_frame_limpio.columns:
        salarios = data_frame_limpio["salario"].dropna()
        if not salarios.empty:
            print("\nSalario mínimo:", salarios.min())
            print("Salario máximo:", salarios.max())
            print("Salario promedio:", salarios.mean())
            print("Salario mediano:", salarios.median())

    if "nombre" in data_frame_limpio.columns:
        print("\nCantidad de empleados únicos por nombre:")
        print(data_frame_limpio["nombre"].nunique())

    print("\n*** PRIMERAS FILAS DEL DATASET ***")
    print(data_frame_limpio.head(10).to_string(index=False))
    