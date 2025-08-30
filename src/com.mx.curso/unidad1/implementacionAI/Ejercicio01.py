#Implementacion Busqueda Lineal AI

#Mariz de 3 x 3 
import time

def busqueda_lineal_matriz(matriz, objetivo):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == objetivo:
                return (i, j)  # Retorna la posición (fila, columna)
    return None

# Matriz con valores fijos para asegurar que el objetivo está presente
matriz = [[0, 2, 3],
          [0, 255, 0],
          [7, 8, 0],
          [7, 88, 0]
]   
objetivo = 88
start_time = time.time()
resultado = busqueda_lineal_matriz(matriz, objetivo)
end_time = time.time()
if resultado:
    print(f"Elemento {objetivo} encontrado en la posición: {resultado}")
else:
    print(f"Elemento {objetivo} no encontrado en la matriz.")
    print(f"Tiempo de búsqueda: {end_time - start_time:.6f} segundos")