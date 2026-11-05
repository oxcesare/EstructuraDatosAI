import random

def merge(a,b):
    i= j =0
    out =[]
    while i < len(a) and j < len(b):
        # elegir el mayor para obtener orden descendente
        if a[i] > b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    out.extend(a[i:])
    out.extend(b[j:])
    return out

#invocar a la funcion merge 

# 2. Función de ORDENAMIENTO (MergeSort)
def merge_sort(lista):
    # Condición de parada: una lista de 1 o 0 elementos ya está ordenada
    if len(lista) <= 1:
        return lista
        
    # Dividir la lista en dos mitades
    m = len(lista) // 2
    
    # Recursividad: ordenar las mitades y luego mezclarlas
    return merge(merge_sort(lista[:m]), merge_sort(lista[m:]))

# Generar una lista de productos con puntuaciones aleatorias
productos = [("prod_%03d" % i, random.uniform(0, 100)) for i in range(1, 101)]
#Solo tomar los scores mas altos
transform = [(pid, score) for (pid, score) in productos]
ordenados = merge_sort(transform)
top5 = [(pid, score) for (pid, score) in ordenados[:5]]
print("Top 5 productos con mejor puntuación:", top5)

