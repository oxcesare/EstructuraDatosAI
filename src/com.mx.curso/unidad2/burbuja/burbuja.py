def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Ejemplo de uso
numeros = [5, 3, 8, 4, 2]
ordenados = bubble_sort(numeros)
print(ordenados)  # Resultado: [2, 3, 4, 5, 8]