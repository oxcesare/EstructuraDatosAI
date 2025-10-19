import numpy as np

# --- 1. Cargar el Conjunto de Datos (Manteniendo tu selección de 5 columnas) ---
# Nota: Incluye '?' como NaN. El dtype 'object' solo debe usarse si tienes texto.
# Mejor forzar a float y especificar el manejo de '?'
datos_brutos = np.genfromtxt('src/com.mx.curso/unidad1/matriz/numpy/practica_numpy_4/processed.cleveland.data',
                             delimiter=',',
                             dtype=float, # Asegura tipo float
                             usecols=(0, 1, 2, 3, 4), # Carga tus 5 columnas: 0, 1, 2, 3, 4
                             missing_values='?', # Indica que '?' es un valor faltante
                             filling_values=np.nan) # Remplaza '?' por np.nan

matriz_inicial = datos_brutos.copy()
filas, columnas = matriz_inicial.shape

# --- 2. Introducir y Manejar Valores Faltantes ---

# 2.a. Introducir np.nan en dos posiciones aleatorias
np.random.seed(42) # Fija la semilla para reproducibilidad

idx_fila_rand = np.random.randint(0, filas, 2)
idx_col_rand = np.random.randint(0, columnas, 2)

matriz_inicial[idx_fila_rand[0], idx_col_rand[0]] = np.nan
matriz_inicial[idx_fila_rand[1], idx_col_rand[1]] = np.nan
print(f"2.a. NaNs introducidos en: {idx_fila_rand[0], idx_col_rand[0]} y {idx_fila_rand[1], idx_col_rand[1]}")

# 2.b. Identificar valores faltantes
nan_indices = np.argwhere(np.isnan(matriz_inicial))
print(f"2.b. Total de NaNs identificados (originales + 2 introducidos): {len(nan_indices)}")

matriz_limpia = matriz_inicial.copy()

# 2.c. Reemplazar cada np.nan con la mediana de la columna
for col in range(columnas):
    mediana_columna = np.nanmedian(matriz_limpia[:, col]) # Calculamos la mediana ignorando NaNs
    nan_en_columna = np.isnan(matriz_limpia[:, col])      # Identificamos los NaNs
    matriz_limpia[nan_en_columna, col] = mediana_columna  # Imputación

print("2.c. Imputación completada con la mediana de cada columna.")

# --- 3. Análisis Descriptivo ---

# 3.a. Imprimir comparación (Primeras 5 filas y 5 columnas)
print("\n" + "="*60)
print("3.a. Comparación: Matriz ANTES vs. DESPUÉS de la limpieza (Primeras 5 Filas)")
print("\nMatriz ANTES (con NaNs):\n", matriz_inicial[:5, :])
print("-" * 60)
print("Matriz DESPUÉS (Imputada con Mediana):\n", matriz_limpia[:5, :])
print("="*60)

# 3.b. Análisis Descriptivo (Media, Mediana, Desviación estándar)
print("3.b. Análisis Descriptivo (Matriz Limpia)")
columnas_etiquetas = ['Edad (0)', 'Columna 1', 'PA (2)', 'Colesterol (3)', 'FC Máx (4)'] # Ajustado a tus supuestos

# Calcular estadísticas
medias = np.mean(matriz_limpia, axis=0).round(2)
medianas = np.median(matriz_limpia, axis=0).round(2)
desviaciones = np.std(matriz_limpia, axis=0).round(2)

# Mostrar en forma tabular (usando formato simple de numpy)
print(f"{'Atributo':<20} | {'Media':<10} | {'Mediana':<10} | {'Desv. Est.':<10}")
print("-" * 60)
for i in range(columnas):
    print(f"{columnas_etiquetas[i]:<20} | {medias[i]:<10} | {medianas[i]:<10} | {desviaciones[i]:<10}")

# --- 4. Análisis Específico de Salud Cardíaca (Usando tus columnas asumidas) ---

# Columna 3 asumida como Colesterol
columna_colesterol = matriz_limpia[:, 3]
# Columna 2 asumida como Presión Arterial
columna_presion_arterial = matriz_limpia[:, 2]
# Columna 4 asumida como Frecuencia Cardíaca Máxima
columna_frecuencia_cardiaca = matriz_limpia[:, 4]
# Columna 0 es la Edad
columna_edad = matriz_limpia[:, 0]

print("\n" + "="*60)
print("4. Análisis Específico de Salud Cardíaca (Basado en tus 5 columnas)")

# 4.a. Promedio de colesterol
promedio_colesterol = np.mean(columna_colesterol)
print(f"1. Promedio de Colesterol (Col 3): {promedio_colesterol:.2f}")

# 4.b. Porcentaje de pacientes con presión arterial mayor al promedio
promedio_presion = np.mean(columna_presion_arterial)
pacientes_mayor_presion = np.sum(columna_presion_arterial > promedio_presion)
porcentaje_mayor_presion = (pacientes_mayor_presion / filas) * 100

print(f"2. Promedio de Presión Arterial (Col 2): {promedio_presion:.2f}")
print(f"   Porcentaje de pacientes con Presión Arterial > Promedio: {porcentaje_mayor_presion:.2f}%")

# 4.c. Edad del paciente con la mayor frecuencia cardiaca alcanzada
indice_max_frecuencia = np.argmax(columna_frecuencia_cardiaca)
frecuencia_maxima = columna_frecuencia_cardiaca[indice_max_frecuencia]
edad_max_frecuencia = columna_edad[indice_max_frecuencia]

print(f"3. Mayor Frecuencia Cardiaca Máxima (Col 4): {frecuencia_maxima:.0f}")
print(f"   Edad del paciente con la mayor frecuencia cardiaca alcanzada: {edad_max_frecuencia:.0f} años")
print("="*60)