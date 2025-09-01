import numpy as np

# Creación de una matriz 3x3
matriz_A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Acceder a un elemento (fila 1, columna 2)
elemento = matriz_A[1, 2] 

# Modificar un elemento
matriz_A[0, 0] = 99

for fila in matriz_A:
    for elemento in fila:
        print(elemento, end=" ")