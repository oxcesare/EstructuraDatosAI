matriz_A = [
    [0,1,1],
    [2,3,4],
    [5,6,7]]

matriz = [
    [0,1,1],
    [2,3,4],
    [5,6,7]]

# Sumar dos matrices
matriz_C = matriz_A + matriz_A

# Otra forma de imprimir la matriz 
for i in range(len(matriz_C)):
    for j in range(len(matriz_C[i])):
        print(matriz_C[i][j], end=" ")
    print() # Nueva línea después de cada fila