#Ejemplo de busqueda lineal 

import time
import random

def busqueda_lineal(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return True
    return False

# Pruebas con diferentes tamaños de arreglos
sizes = [100, 1000, 10000]

for n in sizes:
    arr = list(range(n)) # crear un arreglo ordenado
    target = 1  # Un elemento que no está en el arreglo para forzar el peor caso
    
    start_time = time.time()
    busqueda_lineal(arr, target)
    end_time = time.time()
    
    print(f"Búsqueda lineal en un arreglo de {n} elementos: {end_time - start_time:.6f} segundos")