#Definimos entradas
entrada = [1,2]

# Matriz de pesos (3 neuronas de entrada, 2 de salida)
pesos = [
    [5,2,7,4],
    [5,2,7,5]
]

# Salida
#salida = [0 for _ in range(len(pesos[0]))]
salida = [0,0,0,0]

for j in range(len(pesos[0])):
    # El bucle interno itera sobre cada elemento de la entrada y cada fila de pesos
    print("valores de j",j)
    for i in range(len(entrada)):
        # Realizamos la multiplicación y la sumamos al total de la salida
        salida[j] += entrada[i] * pesos[i][j]

print("Vector de entrada:", entrada)
print("Matriz de pesos:", pesos)
print("\nSalida (producto punto):", salida)
