#Practica con DataSet Iris
import numpy as np


#Cargar el dataset
datos = np.genfromtxt('src/com.mx.curso/unidad1/matriz/numpy/practica_numpy_4/processed.cleveland.data',
                       delimiter=',', dtype='object')

#Visualizar los datos
print(datos)

#Cargar solo las 4 primeras columnas 
datos_numericos = np.genfromtxt('src/com.mx.curso/unidad1/matriz/numpy/practica_numpy_4/processed.cleveland.data',
                       delimiter=',', usecols=(0, 1, 2, 3, 4), # Carga tus 5 columnas: 0, 1, 2, 3, 4
                             missing_values='?', # Indica que '?' es un valor faltante
                             filling_values=np.nan) # Remplaza '?' por np.nan)

#Visualizar los datos
print(datos_numericos)

datos_numericos[0,0] = np.nan
datos_numericos[4,0] = np.nan

media_columna = np.nanmean(datos_numericos,axis=0)
print(" ----- Media de cada columna ----- ",media_columna)

# Imprimimos la media y la desviación estándar de la matriz final para verificar la consistencia
print("Media por columna:", np.mean(datos_numericos, axis=0).round(2))
print("Desviación estándar por columna:", np.std(datos_numericos, axis=0).round(2))
#Imprimir mediana
print("Mediana por columna:", np.median(datos_numericos, axis=0).round(2))

# Columna que tiene el dato de colesterol
columna_colesterol = datos_numericos[:,3]
print("Columna de colesterol:", columna_colesterol)

#Calcular promedio de colesterol
promedio_colesterol = np.nanmean(columna_colesterol)
print(f"Promedio de colesterol: {promedio_colesterol}")

#Imprimir los pacientes con colesterol mayor al promedio
print("Pacientes con colesterol mayor al promedio:")
for i in range(datos_numericos.shape[0]):
    if columna_colesterol[i] > promedio_colesterol:
        print(f"Paciente {i} con colesterol {columna_colesterol[i]}")

#Edad del paciente con mayor frecuencia cardiaca
columna_frecuencia_cardiaca = datos_numericos[:,2]
print("Columna de frecuencia cardiaca:", columna_frecuencia_cardiaca)
indice_max_frecuencia = np.nanargmax(columna_frecuencia_cardiaca)
print(f"Índice del paciente con mayor frecuencia cardiaca: {indice_max_frecuencia}")
edad_max_frecuencia = datos_numericos[indice_max_frecuencia, 0]
print(f"Edad del paciente con mayor frecuencia cardiaca ({columna_frecuencia_cardiaca[indice_max_frecuencia]}): {edad_max_frecuencia}")










