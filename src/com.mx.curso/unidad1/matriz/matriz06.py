import numpy as np

# Creación de una matriz 3x3
matriz_A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Acceder a un elemento (fila 1, columna 2)
elemento = matriz_A[1, 2] 

# Sumar dos matrices
matriz_C = matriz_A + matriz_A

#imprimo la matriz C
for fila in matriz_C:
    for elemento in fila:
        print(elemento, end=" ")

print("***********")

# Multiplicar cada elemento por un número
matriz_D = matriz_A * 2

# Producto punto (operación fundamental en redes neuronales)
vector_E = np.array([1, 2, 3])
resultado = np.dot(matriz_A, vector_E)