import pandas as pd
import sys
import os

from notebook.consumo_empleado import consumo_empleado
from notebook.limpieza_empleado import limpiar_datos_empleado
from notebook.transformacion_empleado import transformar_datos
from notebook.graficacion_empleado import graficar_lineas, graficar_barras, graficar_torta, graficar_mapa_calor
from notebook.limpieza_bonificacion import limpieza_bonificacion
from notebook.limpieza_nomina import limpiar_datos_nomina
from notebook.limpieza_pagos import limpiar_pagos
from notebook.limpieza_cargos import limpiar_datos_cargo


#empleado
datos_empleados = consumo_empleado()
data_frame_empleados=pd.DataFrame(datos_empleados)
data_frame_limpio_empleados = limpiar_datos_empleado(data_frame_empleados)  
agrupaciones = transformar_datos(data_frame_limpio_empleados)

#bonificacion
data_frame_bonificaciones = pd.DataFrame(datos_deducciones)
data_frame_limpio_bonificaciones = limpieza_bonificacion(data_frame_bonificaciones)

#nomina
data_frame_nomina = pd.DataFrame(datos_nomina) 
data_frame_limpio_nomina = limpiar_datos_nomina(data_frame_nomina)

#pagos
data_frame_pagos = pd.DataFrame(datos_pagos)
data_frame_limpio_pagos = limpiar_pagos(data_frame_pagos)

#cargos
data_frame_cargos = pd.DataFrame(datos_cargos)
data_frame_limpio_cargos = limpiar_datos_cargo(data_frame_cargos)



graficar_barras(
    agrupaciones["empleados_nombre"],
    columna_categorias="nombre",
    columna_valores="cantidad_empleados",
    titulo="Cantidad de empleados por nombre",
    nombre_archivo="barras_empleados.png",
    color_barras="#FF33DD"
)

graficar_lineas(
    agrupaciones["promedio_salario"],
    columna_eje_x="nombre",
    columna_eje_y="salario_promedio",
    titulo="Salario promedio por empleado",
    nombre_archivo="lineas_salario.png",
    color_linea="#27B049"
)

graficar_torta(
    agrupaciones["rangos_salario"],
    columna_etiquetas="rango_salario",
    columna_valores="cantidad",
    titulo="Distribución de rangos salariales",
    nombre_archivo="torta_rangos.png",
    lista_colores=["#FF33DD", "#4CAF50", "#2196F3"]


)

graficar_mapa_calor(
    agrupaciones["tipo_documento"],
    columna_filas="documento",
    columna_columnas="documento",
    columna_valores="cantidad_documentos",
    titulo="Cantidad por tipo de documento",
    nombre_archivo="mapa_calor_documentos.png",
    paleta_color="Blues"
)