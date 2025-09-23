import numpy as np

# 1. Crear el conjunto de datos
# Simular un conjunto de datos de 12x5 con valores aleatorios.
# Usamos un seed para que los valores sean los mismos cada vez que se ejecute.
np.random.seed(42)
datos = np.random.rand(10, 3) * 100

# 2. Simular errores
# Introducir una fila de datos erróneos (por ejemplo, en el índice 5)
datos[5] = [1.0,3.3,1.8] 

# Introducir algunos valores faltantes (np.nan) de forma aleatoria
datos[0, 0] = np.nan
datos[1, 2] = np.nan
datos[7, 1] = np.nan

print("--- Conjunto de datos original con errores ---")
print(datos)

#Valores para axis 
# axis=1 -> columnas
# axis=0 -> filas
# axis = None -> todo el array

datos_limpios = np.delete(datos, 0, axis=1)

print("--- Conjunto de datos limpios despues de procesar ---")
print(datos_limpios)