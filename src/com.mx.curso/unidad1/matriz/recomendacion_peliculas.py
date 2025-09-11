# Matriz de recomendacion de peliculas 

matriz = [

    [5,	5,	4,	5,	5,	1,	5,	5,	3,	5,	3,	4,	5],
    [2,	5,	4,	5,	5,	3,	5,	4,	5,	5,	3,	5,	5],
    [2,	5,	5,	5,	4,	3,	5,	4,	4,	5,	2,	4,	5],
    [4,	5,	4,	5,	5,	4,	4,	5,	5,	5,	3,	4,	5],
    [5,	4,	4,	5,	5,	4,	5,	5,	3,	5,	1,	5,	5],
    [3,	5,	3,	5,	3,	5,	2,	1,	3,	5,	3,	1,	5],
    [2,	4,	5,	3,	5,	2,	5,	3,	3,	4,	1,	3,	5],
    [4,	5,	5,	2,	5,	1,	3,	5,	5,	4,	3,	1,	5],
    [3,	2,	5,	2,	5,	2,	3,	2,	5,	4,	5,	4,	5],
    [3,	5,	2,	5,	3,	1,	1,	5,	1,	5,	3,	1,	5],
    [5,	1,	5,	5,	5,	4,	4,	1,	4,	5,	4,	1,	5],
    [5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5],
    [5,	4,	3,	5,	5,	1,	4,	2,	3,	5,	2,	1,	5]
]

#imprimir la matriz de calificaciones
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end="")
    print()    

#Promedio de una pelicula 
suma=0
pelicula=12

for i in range(len(matriz)):
    suma +=  int(matriz[i][pelicula])

print("la suma de calificaciones pelicula 1 ", suma) 
promedio = suma / len(matriz)
print("El promedio  de calificaciones pelicula 1 ", promedio) 

calificacionesUsuario= matriz[6]
print("Calificaciones usuario 0 ", calificacionesUsuario) 