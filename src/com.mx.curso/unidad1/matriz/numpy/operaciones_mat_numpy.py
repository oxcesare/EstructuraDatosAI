import numpy as np

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

# Multiplicar cada elemento por un número
matriz_D = matriz_A * 2

# Producto punto (operación fundamental en redes neuronales)
vector_E = np.array([1, 2, 3])
resultado = np.dot(matriz_A, vector_E)