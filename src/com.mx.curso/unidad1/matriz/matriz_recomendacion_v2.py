# Matriz de recomendaciones de películas
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

# Imprimir la matriz completa
print("--- Matriz de Calificaciones ---")
for fila in matriz:
    for calificacion in fila:
        print(calificacion, end=" ")
    print()

# --- 1. Calcular promedio de una película ---
pelicula_a_promediar = 2  # El índice de la película que queremos (la tercera)
suma_calificaciones = 0
num_usuarios = len(matriz)

# Recorre las filas para sumar la columna de la película
for i in range(num_usuarios):
    suma_calificaciones += matriz[i][pelicula_a_promediar]

# Calcula el promedio de forma precisa con float
promedio_pelicula = suma_calificaciones / float(num_usuarios)

print(f"\n--- Promedio de la película en la columna {pelicula_a_promediar} ---")
print(f"Suma de calificaciones: {suma_calificaciones}")
print(f"Promedio: {promedio_pelicula:.2f}")

# --- 2. Mostrar calificaciones de un usuario ---
usuario_a_mostrar = 5  # El índice del usuario que queremos (el sexto)
if usuario_a_mostrar < num_usuarios:
    # Accede directamente a la fila del usuario
    calificaciones_usuario = matriz[usuario_a_mostrar]
    print(f"\n--- Calificaciones del usuario {usuario_a_mostrar} ---")
    print(calificaciones_usuario)
else:
    print(f"\nEl usuario en el índice {usuario_a_mostrar} no existe.")