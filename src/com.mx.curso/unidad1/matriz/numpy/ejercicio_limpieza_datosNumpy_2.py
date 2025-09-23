import numpy as np

# 1. Crear el conjunto de datos
# Simular un conjunto de datos de 12x5 con valores aleatorios.
# Usamos un seed para que los valores sean los mismos cada vez que se ejecute.
np.random.seed(42)
datos = np.random.rand(12, 5) * 100

# 2. Simular errores
# Introducir una fila de datos erróneos (por ejemplo, en el índice 5)
datos[5] = 999 

# Introducir algunos valores faltantes (np.nan) de forma aleatoria
datos[1, 1] = np.nan
datos[3, 2] = np.nan
datos[9, 4] = np.nan

print("--- Conjunto de datos original con errores ---")
print(datos)

# Encontrar el valor maximo 
max_valor = np.max(datos)
print(f"\nValor maximo en el conjunto de datos: {max_valor}")

# --- Encontrar el valor minimo
min_valor = np.min(datos)
print(f"Valor minimo en el conjunto de datos: {min_valor}")


# 3. Eliminar la fila errónea
# Identificamos la fila con los datos erróneos (por ejemplo, el valor 999).
# np.any() nos ayuda a encontrar si al menos un elemento en una fila es 999.
fila_erronea_idx = np.where(np.any(datos == 999, axis=1))[0]

# Usamos np.delete para eliminar la fila completa.
# axis=0 indica que se debe eliminar la fila (eje vertical).
datos_sin_errores = np.delete(datos, fila_erronea_idx, axis=0)

print("\n--- Datos con fila errónea eliminada ---")
print(datos_sin_errores)

# ---

# 5. Validar y mostrar
# Verificamos si aún hay valores NaN.
print("\nVerificación final:")
print("Valores NaN restantes:", np.sum(np.isnan(datos_sin_errores)))

# Imprimimos la media de la matriz final para verificar la consistencia.
print("Media por columna:", np.mean(datos_sin_errores, axis=0).round(2))