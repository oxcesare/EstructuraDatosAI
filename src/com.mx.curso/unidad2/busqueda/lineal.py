def busqueda_secuencial(arr, x):
    """
    Realiza la búsqueda secuencial (lineal) de un elemento (x) en un arreglo (arr).
    Retorna el índice del elemento si se encuentra, o -1 si no.
    Complejidad Temporal: O(n)
    """
    # Python usa el 'for' de forma más concisa para iterar sobre índices.
    # El bucle recorre todos los índices desde 0 hasta la longitud del arreglo - 1.
    for i in range(len(arr)):
        # Si el elemento en la posición 'i' es igual al buscado 'x', retorna el índice.
        if arr[i] == x:
            return i
            
    # Si el bucle termina sin encontrar el elemento, retorna -1.
    return -1

# --- Ejemplo de Uso (Función principal simulada) ---
if __name__ == "__main__":
    datos = [4, 2, 7, 1, 9, 3, 5]
    elemento_a_buscar = 9

    indice = busqueda_secuencial(datos, elemento_a_buscar)

    if indice != -1:
        print(f"El elemento {elemento_a_buscar} se encuentra en el índice: {indice}")
    else:
        print(f"El elemento {elemento_a_buscar} no se encuentra en el arreglo.")

    # Ejemplo de un elemento que no existe
    otro_elemento = 10
    otro_indice = busqueda_secuencial(datos, otro_elemento)
    print(f"\nBuscando el elemento {otro_elemento}...")
    if otro_indice != -1:
        print(f"El elemento {otro_elemento} se encuentra en el índice: {otro_indice}")
    else:
        print(f"El elemento {otro_elemento} no se encuentra en el arreglo.")