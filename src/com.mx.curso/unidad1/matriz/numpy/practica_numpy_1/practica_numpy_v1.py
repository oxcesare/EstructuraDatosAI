# Leer un archivo csv con numpy
import numpy as np

# 1. Cargar datos desde el archivo iris.data
# El archivo 'iris.data' debe estar en el mismo directorio que este script.
datos = np.genfromtxt('src/com.mx.curso/unidad1/matriz/numpy/practica_numpy_1/iris.data', delimiter=',', dtype=None, encoding='utf-8')

print("--- Conjunto de datos cargado desde iris.data ---")
print(datos)

# cargar solo las 4 columnas numericas de la matriz 
datos_numericos = np.genfromtxt('src/com.mx.curso/unidad1/matriz/numpy/practica_numpy_1/iris.data', delimiter=',', usecols=(0,1,2,3))

print("\n--- Solo las columnas numericas ---")
print(datos_numericos)

#Listado de indices a eliminar 
indices_a_eliminar = [0, 50, 100]

#Simular y eliminar una Fila Errónea 
datos_limpios = np.delete(datos_numericos, indices_a_eliminar, axis=0)

print("\n--- Se imprime los datos sin la fila con errores ---")
print(datos_limpios)

#Simulamos el escenario de agregar filas con valores NaN
datos_limpios[0, 0] = np.nan
datos_limpios[4, 2] = np.nan    
datos_limpios[7, 3] = np.nan

print("\n--- Se imprime matriz con datos NaN ---")
print(datos_limpios)

indices_a_eliminar=[0,4,7]
#Simular y eliminar una Fila Errónea 
datos_limpios = np.delete(datos_numericos, indices_a_eliminar, axis=0)

print("\n--- Se imprime matriz sin datos NaN ---")
print(datos_limpios)