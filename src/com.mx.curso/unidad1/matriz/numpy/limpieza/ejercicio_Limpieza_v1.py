import numpy as np

# 1. Crear el conjunto de datos
# Simular un conjunto de datos de 12x5 con valores aleatorios.
# Usamos un seed para que los valores sean los mismos cada vez que se ejecute.
np.random.seed(42)
datos = np.random.rand(12, 5) * 100

# 2. Simular errores
# Introducir una fila de datos erróneos (por ejemplo, en el índice 5)
datos[5] = [1,3,2,1,1] 

# Introducir algunos valores faltantes (np.nan) de forma aleatoria
datos[1, 1] = np.nan
datos[3, 2] = np.nan
datos[9, 4] = np.nan

print("--- Conjunto de datos original con errores ---")
print(datos)

