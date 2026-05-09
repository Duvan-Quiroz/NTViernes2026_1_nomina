import pandas as pd

#Importar simulaciones
from utils.simulacion_bonificacion import generar_bonificacion
from utils.simulacion_empleado import crear_empleados
from utils.simulacion_nomina import generar_nomina
from utils.simulacion_pagos import generar_pagonomina
from utils.simulacionDeduccion import generar_deduccion
from utils.sumilacion_cargos import generar_cargos

#Importar limpieza
from notebook.limpieza_empleado import limpiar_datos_empleado
from notebook.limpieza_pagos import limpiar_pagos


#Importar descripcion
from notebook.descripcion_empleado import describir_empleados
from notebook.descripcion_pago import describir_pagos



#Creador de simulaciones
simulacion_bonificacion=generar_bonificacion(100)
simulacion_empleado=crear_empleados(100)
simulacion_nomina=generar_nomina(100)
simulacion_pagonomina=generar_pagonomina(100)
simulacion_deduccion=generar_deduccion(100)
simulacion_cargos=generar_cargos(100)


#Ordenar Simulaciones
simulaciones_ordenadas=pd.DataFrame(simulacion_bonificacion)
simulaciones_ordenadas=pd.DataFrame(simulacion_empleado)
simulaciones_ordenadas=pd.DataFrame(simulacion_nomina)
simulaciones_ordenadas=pd.DataFrame(simulacion_pagonomina)
simulaciones_ordenadas=pd.DataFrame(simulacion_deduccion)
simulaciones_ordenadas=pd.DataFrame(simulacion_cargos)


#limpiador Set de datos
simulaciones_limpias=limpiar_datos_empleado(simulacion_empleado)
simulaciones_limpias_pagos=limpiar_pagos(simulacion_pagonomina)

#Descripcion de datos
describir_empleados(simulaciones_limpias)
describir_pagos(simulaciones_limpias_pagos)
