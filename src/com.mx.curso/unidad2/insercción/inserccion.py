def insertion_sort(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

# Ejemplo de uso
numeros = [7, 2, 4, 9, 1]
ordenados = insertion_sort(numeros)
print(ordenados)  # Resultado: [1, 2, 4, 7, 9]