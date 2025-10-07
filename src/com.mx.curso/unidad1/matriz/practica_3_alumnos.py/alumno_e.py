# Crear la matriz de calificaciones (nx3)
tablero = [     # filas (estudiantes), columnas(calificaciones)
    [9,8,8],
    [7,8,6],
    [8,8,8],
    [9,9,10],
    [10,10,10]
]

# Calcular y mostrar el promedio de cada estudiante en un vector.
promedios_estudiantes = []
for f in range(len(tablero)):
    promedio = 0
    for c in range(len(tablero[f])):
        promedio += tablero[f][c]
    promedio = promedio / len(tablero[f])
    promedios_estudiantes.append(promedio)

print("Promedios de los estudiantes:", promedios_estudiantes)

# Calcular el promedio de cada examen (columna).
promedios_examenes = []
for c in range(len(tablero[0])):
    promedio = 0
    for f in range(len(tablero)):
        promedio += tablero[f][c]
    promedio = promedio / len(tablero)
    promedios_examenes.append(promedio)

print("Promedios de los examenes:", promedios_examenes)

# Determinar qué estudiante obtuvo la calificación más alta en el curso.
print("Calificación mas alta del curso:", max(promedios_estudiantes))