#Comentario
import numpy as np

# 1. Crear un conjunto de datos (matriz de 3x4)
# La segunda columna (índice 1) es la que se eliminará.
datos = np.array([
    [-1, 20, 30, 40],
    [15, 20, 35, 45],
    [15, 20, 35, 45],
    [15, 20, 35, -45],
    [25, 20, -45, 55]
])

print("--- Conjunto de datos original ---")
print(datos)

# Interar la matriz y mostrar cada fila
for fila in datos:
    print("Fila:", fila)
    for elemento in fila:
        print("  Elemento:", elemento)
    print("")    

# Almacenar en un arreglo los indices donde se encuentren valores negativos
valores_negativos = []
for i in range(datos.shape[0]):  # Iterar sobre las filas
    for j in range(datos.shape[1]):  # Iterar sobre las columnas
        if datos[i, j] < 0:
            valores_negativos.append(i)
            break  # No es necesario seguir buscando en esta fila   

print("Indices con valores negativos:", valores_negativos)

# Ya con los datos negativos vamos a eliminar esa fila donde se encuentren esos valores
#Simular y eliminar una Fila Errónea 
datos_limpios = np.delete(datos, valores_negativos, axis=0)

# Imprimos la mariz con datos limpios
print("--- Conjunto de datos Limpios ---")
print(datos_limpios)