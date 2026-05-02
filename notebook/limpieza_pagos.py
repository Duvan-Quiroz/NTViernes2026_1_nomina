import pandas as pd


def limpiar_pagos(pagos):
    df = pd.DataFrame(pagos).copy()
    df.columns = df.columns.str.strip().str.lower()

    if "metodo" in df.columns:
        df["metodo"] = df["metodo"].astype("string").str.strip().str.lower()

    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
    df["id_pago"] = pd.to_numeric(df["id_pago"], errors="coerce").astype("Int64")
    df["id_empleado"] = pd.to_numeric(df["id_empleado"], errors="coerce").astype("Int64")

    df["valor"] = df["valor"].abs()

    columnas_obligatorias = ["id_pago", "id_empleado", "valor"]
    df = df.dropna(subset=columnas_obligatorias)

    df = df[(df["id_pago"] > 0) & (df["id_empleado"] > 0) & (df["valor"] > 0)]

    if "metodo" in df.columns:
        df = df[df["metodo"].notna() & (df["metodo"].str.strip() != "")]

    df = df.drop_duplicates()
    return df

