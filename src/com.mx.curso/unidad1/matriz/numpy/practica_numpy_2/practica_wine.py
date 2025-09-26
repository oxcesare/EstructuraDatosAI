# Leer un archivo csv con numpy
import numpy as np

# 1. Cargar datos desde el archivo winequality-red.csv
# El archivo 'winequality-red.csv' debe estar en el mismo directorio que este script.
datos = np.genfromtxt('src/com.mx.curso/unidad1/matriz/numpy/practica_numpy_2/winequality-red.csv', delimiter=',', dtype=None, encoding='utf-8')

print("El arreglo tiene la siguiente forma (filas, columnas):", datos.shape)
print("--- Conjunto de datos cargado desde winequality-red.csv ---")
print(datos)

# Cargar solo las 4 primeras columnas numéricas de la matriz
datos_numericos = np.genfromtxt(
    'src/com.mx.curso/unidad1/matriz/numpy/practica_numpy_2/winequality-red.csv',
    delimiter=';',          # <-- Delimitador corregido a punto y coma
    skip_header=1,          # <-- Se agrega para omitir la primera fila (encabezado)
    usecols=(0, 1, 2, 3)    # <-- Las columnas que se desean cargar
)

print("\n--- Columnas numéricas cargadas correctamente ---")
print(datos_numericos)


#Simulamos el escenario de agregar filas con valores NaN
datos_numericos[0, 0] = np.nan
datos_numericos[0, 2] = np.nan    
datos_numericos[1, 3] = np.nan

print("\n--- Se imprime matriz con datos NaN ---")
print(datos_numericos)

