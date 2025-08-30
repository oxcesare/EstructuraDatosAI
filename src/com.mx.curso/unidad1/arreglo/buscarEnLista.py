def buscar_elemento(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    return False

#invocar la funcion
mi_lista = [1, 2, 3, 4, 5]
elemento_a_buscar = 3
encontrado = buscar_elemento(mi_lista, elemento_a_buscar)
print(f"Elemento {elemento_a_buscar} encontrado: {encontrado}")