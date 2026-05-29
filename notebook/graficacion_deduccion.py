
# Se importa matplotlib para crear los gráficos
import matplotlib.pyplot as plt
# Se importa seaborn para el mapa de calor con estilo mejorado
import seaborn as sns
# Se importa os para manejar rutas y crear carpetas
import os
import pandas as pd

# Ruta donde se guardarán los gráficos dentro de tu proyecto Python
RUTA_ASSETS = os.path.join(os.path.dirname(__file__), "graficos")

def crear_ruta_si_no_existe(ruta_destino):
    os.makedirs(ruta_destino, exist_ok=True)

def graficar_lineas(datos_agrupados, columna_eje_x, columna_eje_y,
                    titulo="Gráfico de líneas de deducciones", color_linea="#E91E63",
                    nombre_archivo="deducciones_lineas.png", ruta_destino=RUTA_ASSETS):
    crear_ruta_si_no_existe(ruta_destino)
    figura, area_dibujo = plt.subplots(figsize=(10, 5))
    area_dibujo.plot(
        datos_agrupados[columna_eje_x],
        datos_agrupados[columna_eje_y],
        marker="o",
        color=color_linea,
        linewidth=2
    )
    area_dibujo.set_title(titulo, fontsize=14)
    area_dibujo.set_xlabel(columna_eje_x, fontsize=12)
    area_dibujo.set_ylabel(columna_eje_y, fontsize=12)
    area_dibujo.grid(True, linestyle="--", alpha=0.6)
    plt.xticks(rotation=45)
    plt.tight_layout()
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Gráfico de líneas guardado en: {ruta_completa}")

def graficar_barras(datos_agrupados, columna_categorias, columna_valores,
                    titulo="Gráfico de barras de deducciones", color_barras="#9C27B0",
                    nombre_archivo="deducciones_barras.png", ruta_destino=RUTA_ASSETS):
    crear_ruta_si_no_existe(ruta_destino)
    figura, area_dibujo = plt.subplots(figsize=(10, 5))
    area_dibujo.bar(
        datos_agrupados[columna_categorias],
        datos_agrupados[columna_valores],
        color=color_barras,
        edgecolor="black"
    )
    area_dibujo.set_title(titulo, fontsize=14)
    area_dibujo.set_xlabel(columna_categorias, fontsize=12)
    area_dibujo.set_ylabel(columna_valores, fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Gráfico de barras guardado en: {ruta_completa}")

def graficar_torta(datos_agrupados, columna_etiquetas, columna_valores,
                   titulo="Gráfico de torta de deducciones", lista_colores=None,
                   nombre_archivo="deducciones_torta.png", ruta_destino=RUTA_ASSETS):
    crear_ruta_si_no_existe(ruta_destino)
    if lista_colores is None:
        lista_colores = ["#FF9800", "#2196F3", "#4CAF50", "#E91E63", "#9C27B0"]
    figura, area_dibujo = plt.subplots(figsize=(8, 8))
    cantidad_categorias = len(datos_agrupados)
    area_dibujo.pie(
        datos_agrupados[columna_valores],
        labels=datos_agrupados[columna_etiquetas],
        autopct="%1.1f%%",
        colors=lista_colores[:cantidad_categorias],
        startangle=90,
        wedgeprops={"edgecolor": "black", "linewidth": 0.5}
    )
    area_dibujo.set_title(titulo, fontsize=14)
    plt.tight_layout()
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Gráfico de torta guardado en: {ruta_completa}")

def graficar_mapa_calor(datos_agrupados, columna_filas, columna_columnas, columna_valores,
                        titulo="Mapa de calor de deducciones", paleta_color="YlOrRd",
                        nombre_archivo="deducciones_mapa_calor.png", ruta_destino=RUTA_ASSETS):
    crear_ruta_si_no_existe(ruta_destino)
    tabla_pivote = datos_agrupados.pivot_table(
        index=columna_filas,
        columns=columna_columnas,
        values=columna_valores,
        aggfunc="sum",
        fill_value=0
    )
    figura, area_dibujo = plt.subplots(figsize=(10, 6))
    sns.heatmap(
        tabla_pivote,
        annot=True,
        fmt=".0f",
        cmap=paleta_color,
        ax=area_dibujo,
        linewidths=0.5,
        linecolor="gray"
    )
    area_dibujo.set_title(titulo, fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Mapa de calor guardado en: {ruta_completa}")

# --- Transformaciones de datos ---
def transformar_datos(data_frame_limpio):
    # Transformación 1 (conteo por id)
    filtro1 = data_frame_limpio
    agrupacion1 = filtro1.groupby("id")["valor"].count().reset_index(name="cantidad_deducciones")

    # Transformación 2 (valor promedio por id)
    filtro2 = data_frame_limpio
    agrupacion2 = filtro2.groupby("id")["valor"].mean().reset_index(name="valor_promedio")

    # Transformación 3 (deducciones con valor alto >30)
    filtro3 = data_frame_limpio.query("valor > 30")
    agrupacion3 = filtro3.groupby("id")["valor"].count().reset_index(name="cantidad_valor_alto")

    # Transformación 4 (rangos de valor)
    filtro4 = data_frame_limpio.copy()
    filtro4["rango_valor"] = pd.cut(
        filtro4["valor"],
        bins=[0, 20, 50, 100],
        labels=["Bajo", "Medio", "Alto"]
    )
    agrupacion4 = filtro4.groupby("rango_valor")["id"].count().reset_index(name="cantidad")

    # Transformación 5 (total deducido por id)
    filtro5 = data_frame_limpio
    agrupacion5 = filtro5.groupby("id")["valor"].sum().reset_index(name="total_deducido")

    return {
        "deducciones_id": agrupacion1,
        "promedio_valor": agrupacion2,
        "valor_alto": agrupacion3,
        "rangos_valor": agrupacion4,
        "total_deducido": agrupacion5
    }