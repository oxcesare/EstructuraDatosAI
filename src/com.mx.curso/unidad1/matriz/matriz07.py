import numpy as np

# Creación de una matriz 3x3
matriz_A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
# Transponer la matriz (cambiar filas por columnas)
matriz_transpuesta = matriz_A.T

# Cambiar la forma de una matriz
# Aplanar una matriz ( significa convertirla en un vector)
matriz_aplanada = matriz_A.flatten()


print("Matriz Transpuesta:")
for fila in matriz_transpuesta:
    for elemento in fila:
        print(elemento, end=" ")

print("\n***********")

print("\nMatriz Aplanada:")
for elemento in matriz_aplanada:
    print(elemento, end=" ")