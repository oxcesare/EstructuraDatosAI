def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        #ASignar a pivote el tamaño de la lista menos uno        
        pivote = lista[lista.len() - 1]
        menores = [x for x in lista[1:] if x[1] <= pivote[1]]
        mayores = [x for x in lista[1:] if x[1] > pivote[1]]
        return quicksort(menores) + [pivote] + quicksort(mayores)

comentarios = [
    ("Me encantó el producto", 0.9),
    ("No funcionó como esperaba", 0.3),
    ("Excelente servicio", 0.95),
    ("Podría ser mejor", 0.5),
    ("Muy decepcionado", 0.1)
]

comentarios_ordenados = quicksort(comentarios)


print("Comentarios ordenados por puntuación de sentimiento (menor a mayor):")
for comentario, puntuacion in comentarios_ordenados:
    print(f"{comentario}: {puntuacion}")
