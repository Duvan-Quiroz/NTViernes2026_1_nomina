import pandas as pd


def describir_pagos(data_frame_pagos):
    """Describe un DataFrame de pagos con estadísticas, conteos y agregaciones."""

    if data_frame_pagos is None:
        print("No se recibió ningún DataFrame de pagos para describir.")
        return

    if isinstance(data_frame_pagos, list):
        data_frame_pagos = pd.DataFrame(data_frame_pagos)
    elif not isinstance(data_frame_pagos, pd.DataFrame):
        try:
            data_frame_pagos = pd.DataFrame(data_frame_pagos)
        except Exception as e:
            print(f"No se pudo convertir el input de pagos a DataFrame: {e}")
            return

    df = data_frame_pagos.copy()
    df.columns = df.columns.str.strip().str.lower()

    if "metodo" in df.columns:
        df["metodo"] = df["metodo"].astype("string").str.strip().str.lower()

    if "valor" in df.columns:
        df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
        df["valor"] = df["valor"].abs()

    for columna in ["id_pago", "id_empleado"]:
        if columna in df.columns:
            df[columna] = pd.to_numeric(df[columna], errors="coerce").astype("Int64")

    print("*** DESCRIPCION DEL DATASET DE PAGOS ***")
    print(f"Número de filas del dataset: {df.shape[0]}")
    print(f"Número de columnas del dataset: {df.shape[1]}")
    print(f"Columnas disponibles: {list(df.columns)}")
    print("Tipos de dato de cada atributo:")
    print(df.dtypes)

    print("\n*** VALORES FALTANTES ***")
    faltantes = df.isna().sum()
    print(faltantes[faltantes > 0] if faltantes.any() else "No hay valores faltantes.")

    print("\n*** ESTADÍSTICAS NUMÉRICAS ***")
    try:
        print(df.select_dtypes(include=["number"]).describe())
    except Exception as e:
        print(f"No se pudieron calcular estadísticas numéricas: {e}")

    print("\n*** RESUMEN DE COLUMNAS CLAVE ***")
    columnas_clave = ["id_pago", "id_empleado", "valor", "metodo"]
    for columna in columnas_clave:
        if columna in df.columns:
            print(f"\n-- {columna} --")
            if pd.api.types.is_numeric_dtype(df[columna].dtype):
                print(df[columna].describe())
            else:
                print(df[columna].value_counts(dropna=False))
        else:
            print(f"La columna '{columna}' no está presente en el dataset.")

    if "metodo" in df.columns and not df["metodo"].isna().all():
        print("\n*** PAGOS POR METODO ***")
        print(df["metodo"].value_counts(dropna=False))

        if "valor" in df.columns and not df["valor"].isna().all():
            try:
                pagos_por_metodo = df.groupby("metodo")["valor"].agg(["count", "sum", "mean", "min", "max"])
                print("\nEstadísticas de valor por método de pago:")
                print(pagos_por_metodo)
            except Exception as e:
                print(f"No se pudieron calcular agregados por método: {e}")

    if "id_empleado" in df.columns and "valor" in df.columns:
        top_empleados = df.groupby("id_empleado")["valor"].sum().sort_values(ascending=False).head(10)
        print("\n*** TOP 10 EMPLEADOS POR SUMA DE PAGOS ***")
        print(top_empleados)

    print("\n*** PRIMERAS FILAS DEL DATASET DE PAGOS ***")
    print(df.head(10).to_string(index=False))
