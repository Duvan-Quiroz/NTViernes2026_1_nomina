import pandas as pd

#**********************EMPLEADOS ***********************
from notebook.consumo_empleado import consumo_empleado
from notebook.limpieza_empleado import limpiar_datos_empleado
from notebook.transformacion_empleado import transformar_datos as transformar_empleados
from notebook.graficacion_empleado import graficar_lineas as lineas_empleado
from notebook.graficacion_empleado import graficar_barras as barras_empleado
from notebook.graficacion_empleado import graficar_torta as torta_empleado
from notebook.graficacion_empleado import graficar_mapa_calor as calor_empleado

#**********************BONIFICACIONES ***********************
from notebook.consumo_bonificacion import consumo_bonificacion
from notebook.limpieza_bonificacion import limpieza_bonificacion
from notebook.transformacion_bonificacion import transformar_datos as transformar_bonificaciones
from notebook.graficacion_bonificacion import graficar_barras as barras_bonificacion
from notebook.graficacion_bonificacion import graficar_lineas as lineas_bonificacion
from notebook.graficacion_bonificacion import graficar_torta as torta_bonificacion
from notebook.graficacion_bonificacion import graficar_mapa_calor as calor_bonificacion

#**********************NOMINA ***********************
from notebook.consumo_nomina import consumo_nomina
from notebook.limpieza_nomina import limpiar_datos_nomina
from notebook.transformacion_nomina import transformar_datos as transformar_nomina
from notebook.graficacion_nomina import graficar_barras as barras_nomina
from notebook.graficacion_nomina import graficar_lineas as lineas_nomina
from notebook.graficacion_nomina import graficar_torta as torta_nomina
from notebook.graficacion_nomina import graficar_mapa_calor as calor_nomina

#**********************PAGOS ***********************
from notebook.consumo_pago import consumo_pago
from notebook.limpieza_pagos import limpiar_pagos
from notebook.transformacion_pagos import transformar_datos as transformar_pagos
from notebook.graficacion_pagos import graficar_barras as barras_pago
from notebook.graficacion_pagos import graficar_lineas as lineas_pago
from notebook.graficacion_pagos import graficar_torta as torta_pago
from notebook.graficacion_pagos import graficar_mapa_calor as calor_pago

#**********************CARGOS ***********************
from notebook.consumo_cargos import consumo_cargos
from notebook.limpieza_cargos import limpiar_datos_cargo
from notebook.transformacion_cargos import transformar_datos as transformar_cargos
from notebook.graficacion_cargos import graficar_barras as barras_cargo
from notebook.graficacion_cargos import graficar_torta as torta_cargo


#**********************DEDUCCIONES ***********************
from notebook.consumo_deduccion import consumo_deduccion
from notebook.limpieza_deduccion import limpiar_datos_deduccion
from notebook.transformacion_deduccion import transformar_datos as transformar_deducciones
from notebook.graficacion_deduccion import graficar_barras as barras_deduccion
from notebook.graficacion_deduccion import graficar_lineas as lineas_deduccion
from notebook.graficacion_deduccion import graficar_torta as torta_deduccion
from notebook.graficacion_deduccion import graficar_mapa_calor as calor_deduccion


#**********************EMPLEADOS ***********************
datos_empleados = consumo_empleado()
data_frame_empleados = pd.DataFrame(datos_empleados)
data_frame_limpio_empleados = limpiar_datos_empleado(data_frame_empleados)
agrupaciones_empleados = transformar_empleados(data_frame_limpio_empleados)

#**********************BONIFICACIONES ***********************
datos_bonificaciones = consumo_bonificacion()
data_frame_bonificaciones = pd.DataFrame(datos_bonificaciones)
data_frame_limpio_bonificaciones = limpieza_bonificacion(data_frame_bonificaciones)
agrupaciones_bonificaciones = transformar_bonificaciones(data_frame_limpio_bonificaciones)

#**********************NOMINA ***********************
datos_nomina = consumo_nomina()
data_frame_nomina = pd.DataFrame(datos_nomina)
data_frame_limpio_nomina = limpiar_datos_nomina(data_frame_nomina)
agrupaciones_nomina = transformar_nomina(data_frame_limpio_nomina)

#**********************PAGOS ***********************
datos_pagos = consumo_pago()
data_frame_pagos = pd.DataFrame(datos_pagos)
data_frame_limpio_pagos = limpiar_pagos(data_frame_pagos)
agrupaciones_pagos = transformar_pagos(data_frame_limpio_pagos)

#**********************CARGOS ***********************
datos_cargos = consumo_cargos()
data_frame_cargos = pd.DataFrame(datos_cargos)
data_frame_limpio_cargos = limpiar_datos_cargo(data_frame_cargos)
agrupaciones_cargos = transformar_cargos(data_frame_limpio_cargos)

#**********************DEDUCCIONES ***********************
datos_deducciones = consumo_deduccion()
data_frame_deducciones = pd.DataFrame(datos_deducciones)
data_frame_limpio_deducciones = limpiar_datos_deduccion(data_frame_deducciones)
agrupaciones_deducciones = transformar_deducciones(data_frame_limpio_deducciones)

#**********************EMPLEADOS ***********************
barras_empleado(
    agrupaciones_empleados["empleados_nombre"],
    columna_categorias="nombre",
    columna_valores="cantidad_empleados",
    titulo="Cantidad de empleados por nombre",
    nombre_archivo="barras_empleados.png",
    color_barras="#FF33DD"
)

lineas_empleado(
    agrupaciones_empleados["promedio_salario"],
    columna_eje_x="nombre",
    columna_eje_y="salario_promedio",
    titulo="Salario promedio por empleado",
    nombre_archivo="lineas_salario.png",
    color_linea="#27B049"
)

torta_empleado(
    agrupaciones_empleados["rangos_salario"],
    columna_etiquetas="rango_salario",
    columna_valores="cantidad",
    titulo="Distribución de rangos salariales",
    nombre_archivo="torta_rangos.png",
    lista_colores=["#FF33DD", "#4CAF50", "#2196F3"]
)

calor_empleado(
    agrupaciones_empleados["tipo_documento"],
    columna_filas="documento",
    columna_columnas="documento",
    columna_valores="cantidad_documentos",
    titulo="Cantidad por tipo de documento",
    nombre_archivo="mapa_calor_documentos.png",
    paleta_color="Blues"
)

#**********************BONIFICACIONES ***********************
barras_bonificacion(
    agrupaciones_bonificaciones["bonificaciones_id"],
    columna_categorias="id",
    columna_valores="cantidad_bonificaciones",
    titulo="Cantidad de bonificaciones por id",
    nombre_archivo="barras_bonificacion.png",
    color_barras="#FF9800"
)

lineas_bonificacion(
    agrupaciones_bonificaciones["promedio_valor"],
    columna_eje_x="id",
    columna_eje_y="valor_promedio",
    titulo="Valor promedio por bonificación",
    nombre_archivo="lineas_bonificacion.png",
    color_linea="#4CAF50"
)

torta_bonificacion(
    agrupaciones_bonificaciones["rangos_valor"],
    columna_etiquetas="rango_valor",
    columna_valores="cantidad",
    titulo="Distribución de rangos de bonificación",
    nombre_archivo="torta_bonificacion.png",
    lista_colores=["#FF9800", "#4CAF50", "#2196F3"]
)

calor_bonificacion(
    agrupaciones_bonificaciones["total_bonificado"],
    columna_filas="id",
    columna_columnas="id",
    columna_valores="total_bonificado",
    titulo="Total bonificado por id",
    nombre_archivo="mapa_calor_bonificacion.png",
    paleta_color="Greens"
)

#**********************NOMINA ***********************
barras_nomina(
    agrupaciones_nomina["nominas_id"],
    columna_categorias="id",
    columna_valores="cantidad_nominas",
    titulo="Cantidad de nóminas por empleado",
    nombre_archivo="barras_nomina.png",
    color_barras="#FF9800"
)

lineas_nomina(
    agrupaciones_nomina["nominas_mes"],
    columna_eje_x="mes",
    columna_eje_y="cantidad_nominas_mes",
    titulo="Nóminas por mes",
    nombre_archivo="lineas_nomina.png",
    color_linea="#E91E63"
)

torta_nomina(
    agrupaciones_nomina["rangos_salario"],
    columna_etiquetas="rango_salario",
    columna_valores="cantidad",
    titulo="Distribución de rangos salariales nómina",
    nombre_archivo="torta_nomina.png",
    lista_colores=["#FF9800", "#4CAF50", "#2196F3"]
)

calor_nomina(
    agrupaciones_nomina["promedio_salario"],
    columna_filas="id",
    columna_columnas="id",
    columna_valores="salario_promedio",
    titulo="Salario promedio por empleado",
    nombre_archivo="mapa_calor_nomina.png",
    paleta_color="Oranges"
)

#**********************PAGOS ***********************
barras_pago(
    agrupaciones_pagos["pagos_metodo"],
    columna_categorias="metodo",
    columna_valores="cantidad_pagos",
    titulo="Cantidad de pagos por método",
    nombre_archivo="barras_pagos.png",
    color_barras="#FF9800"
)

lineas_pago(
    agrupaciones_pagos["promedio_valor"],
    columna_eje_x="metodo",
    columna_eje_y="valor_promedio",
    titulo="Valor promedio por método de pago",
    nombre_archivo="lineas_pagos.png",
    color_linea="#2196F3"
)

torta_pago(
    agrupaciones_pagos["rangos_valor"],
    columna_etiquetas="rango_valor",
    columna_valores="cantidad",
    titulo="Distribución de rangos de valor",
    nombre_archivo="torta_pagos.png",
    lista_colores=["#FF9800", "#4CAF50", "#2196F3"]
)

calor_pago(
    agrupaciones_pagos["pagos_empleado"],
    columna_filas="id_empleado",
    columna_columnas="id_empleado",
    columna_valores="total_pagado",
    titulo="Total pagado por empleado",
    nombre_archivo="mapa_calor_pagos.png",
    paleta_color="YlOrRd"
)

#**********************CARGOS ***********************
barras_cargo(
    agrupaciones_cargos["cargos_nombre"],
    columna_categorias="nombre",
    columna_valores="cantidad_cargos",
    titulo="Cantidad de cargos por nombre",
    nombre_archivo="barras_cargos.png",
    color_barras="#2196F3"
)

torta_cargo(
    agrupaciones_cargos["cargos_nombre"],
    columna_etiquetas="nombre",
    columna_valores="cantidad_cargos",
    titulo="Proporción de cargos",
    nombre_archivo="torta_cargos.png",
    lista_colores=["#FF9800", "#4CAF50", "#2196F3", "#E91E63", "#9C27B0", "#FF5733", "#27B049"]
)

#**********************DEDUCCIONES ***********************
barras_deduccion(
    agrupaciones_deducciones["deducciones_id"],
    columna_categorias="id",
    columna_valores="cantidad_deducciones",
    titulo="Cantidad de deducciones por id",
    nombre_archivo="barras_deduccion.png",
    color_barras="#E91E63"
)

lineas_deduccion(
    agrupaciones_deducciones["promedio_valor"],
    columna_eje_x="id",
    columna_eje_y="valor_promedio",
    titulo="Valor promedio por deducción",
    nombre_archivo="lineas_deduccion.png",
    color_linea="#9C27B0"
)

torta_deduccion(
    agrupaciones_deducciones["rangos_valor"],
    columna_etiquetas="rango_valor",
    columna_valores="cantidad",
    titulo="Distribución de rangos de deducción",
    nombre_archivo="torta_deduccion.png",
    lista_colores=["#E91E63", "#4CAF50", "#2196F3"]
)

calor_deduccion(
    agrupaciones_deducciones["total_deducido"],
    columna_filas="id",
    columna_columnas="id",
    columna_valores="total_deducido",
    titulo="Total deducido por id",
    nombre_archivo="mapa_calor_deduccion.png",
    paleta_color="Purples"
)