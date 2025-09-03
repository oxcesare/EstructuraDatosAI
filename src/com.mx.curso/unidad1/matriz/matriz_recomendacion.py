# Matriz de recomendaciones de peliculas

# Crear matriz de 
# ["La vida es bella",
# "Spiderman",
# "Rescatando al soldado Ryan",
# "Contador",
# "El justiciero"],
matriz = [
    [1, 5, 4, 3, 2],
    [1, 5, 4, 3, 2],
    [1, 5, 4, 3, 2],
    [1, 5, 4, 3, 2],
    [1, 5, 4, 3, 2],
    [1, 5, 4, 3, 2],
    [1, 5, 4, 3, 2],
    [1, 5, 4, 3, 2],
    [1, 5, 4, 3, 2],
    [1, 5, 4, 3, 2],
    [1, 5, 4, 3, 2],
    [1, 5, 4, 3, 2],
    [1, 5, 4, 3, 2],
]


#Imprimir la matriz
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print() # Nueva línea después de cada fila

#Promedio de una pelicula 
suma =0     
pelicula=2
for i in range(len(matriz)):    
    suma += int(matriz[i][pelicula])  # Convertir a entero y sumar

calificacionesUsuario=matriz[5]  

print("La suma de las calificaciones es: ", suma)
promedio = suma / len(matriz) # Dividir por el número de usuarios (filas - 1 para excluir la fila de encabezado)
print("El promedio de la pelicula es: ", promedio)
print("Calificaciones del usuario para la pelicula: ", calificacionesUsuario)