def busqueda_binaria(arr, x):
    """
    Realiza la búsqueda binaria de un elemento (x) en un arreglo ordenado (arr).
    Retorna el índice del elemento si se encuentra, o -1 si no.
    Complejidad Temporal: O(log n)
    """
    # Se inicializan los punteros de inicio y fin del arreglo
    inicio = 0
    fin = len(arr) - 1

    # El ciclo se ejecuta mientras el puntero de inicio no exceda al de fin
    while inicio <= fin:
        # Se calcula el punto medio. Se usa división entera (//) en Python.
        # La fórmula 'inicio + (fin - inicio) // 2' evita un posible desbordamiento
        # de entero que podría ocurrir en lenguajes como Java/C++ con arreglos gigantes.
        medio = inicio + (fin - inicio) // 2

        # 1. Si el elemento es el del medio, se retorna el índice
        if arr[medio] == x:
            return medio

        # 2. Si el elemento buscado (x) es mayor que el del medio,
        #    se descarta la mitad izquierda y se mueve 'inicio' a 'medio + 1'
        elif arr[medio] < x:
            inicio = medio + 1

        # 3. Si el elemento buscado (x) es menor que el del medio,
        #    se descarta la mitad derecha y se mueve 'fin' a 'medio - 1'
        else:
            fin = medio - 1

    # Si el bucle termina y no se encontró el elemento, se retorna -1
    return -1

# --- Ejemplo de Uso (Función principal simulada) ---
if __name__ == "__main__":
    datos_ordenados = [1, 2, 4, 7, 9, 12, 15, 18]
    elemento_a_buscar = 9

    indice = busqueda_binaria(datos_ordenados, elemento_a_buscar)

    if indice != -1:
        print(f"El elemento {elemento_a_buscar} se encuentra en el índice: {indice}")
    else:
        print(f"El elemento {elemento_a_buscar} no se encuentra en el arreglo.")

    # Ejemplo de un elemento que no existe
    otro_elemento = 10
    otro_indice = busqueda_binaria(datos_ordenados, otro_elemento)
    print(f"\nBuscando el elemento {otro_elemento}...")
    if otro_indice != -1:
        print(f"El elemento {otro_elemento} se encuentra en el índice: {otro_indice}")
    else:
        print(f"El elemento {otro_elemento} no se encuentra en el arreglo.")