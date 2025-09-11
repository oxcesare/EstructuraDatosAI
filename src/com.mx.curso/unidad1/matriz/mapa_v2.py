# Mapa de Riesgo para la Navegación de un Vehículo Autónomo

#Crear matriz de 8x8
matriz = [
    [0,1,0,1,1,1,0,1],
    [0,1,0,1,1,1,0,1],
    [0,1,0,1,1,1,0,1],
    [0,1,0,1,2,1,0,1],
    [0,1,0,1,1,1,0,1],
    [0,1,0,1,2,1,0,0],
    [0,1,2,1,1,1,0,0],
    [0,1,0,1,2,1,0,0]
]

# Otra forma de imprimir la matriz 
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print() # Nueva línea después de cada fila