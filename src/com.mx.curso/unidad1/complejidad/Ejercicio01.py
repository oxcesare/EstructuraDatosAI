#Analisis de complejidad

def buscar_elemento(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    return False

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento_a_buscar = 3
encontrado = buscar_elemento(mi_lista, elemento_a_buscar)
print(f"Elemento {elemento_a_buscar} encontrado: {encontrado}")