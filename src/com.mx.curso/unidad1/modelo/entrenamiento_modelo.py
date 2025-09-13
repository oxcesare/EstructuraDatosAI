#Historial de Entrenamiento de un Modelo

# Métrica de precisión del modelo por época
# Las precisiones pueden ser generadas aleatoriamente o predefinidas
metricas_precision = [
    0.75,  # Precisión en la época 1
    0.81,  # Precisión en la época 2
    0.83,  # Precisión en la época 3
    0.85,  # Precisión en la época 4
    0.86,  # Precisión en la época 5
    0.87,  # Precisión en la época 6
    0.89,  # Precisión en la época 7
    0.97,  # Precisión en la época 8
    0.92,  # Precisión en la época 9
    0.91,  # Precisión en la época 10
    0.93,  # Precisión en la época 11
]

# Imprimimos  metricas antes de su entrenamiento
print(metricas_precision)

# Se agrega una precisión al modelo
metricas_precision.append(0.82)

# Imprimimos nuevamente las metricas 
print(metricas_precision)

#Se definen precisiones nuevas 
precisiones_nuevas = [0.81, 0.83, 0.85, 0.86, 0.87]

for i in precisiones_nuevas:
    metricas_precision.append(i)

#Precisión más alta alcanzada
presicion_final = metricas_precision[-1]

print("Precision final", presicion_final)

# Mostrar la precisión más alta alcanzada
precision_mas_alta = max(metricas_precision)
print("Precisión más alta alcanzada:", precision_mas_alta)