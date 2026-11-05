
# Ejercicio: Calificaciones de estudiantes con matriz y vectores

# Pedir número de estudiantes
num_estudiantes = int(input("¿Cuántos estudiantes hay? "))

# Crear matriz para guardar calificaciones (filas: estudiantes, columnas: exámenes)
calificaciones = []

# Ingresar calificaciones de cada estudiante
for i in range(num_estudiantes):
    print(f"\nEstudiante {i+1}:")
    fila = []
    for j in range(3):
        nota = float(input(f"  Calificación del examen {j+1}: "))
        fila.append(nota)
    calificaciones.append(fila)

# Calcular y mostrar el promedio de cada estudiante
promedios_estudiantes = []
print("\nPromedio de cada estudiante:")
for i in range(num_estudiantes):
    promedio = sum(calificaciones[i]) / 3
    promedios_estudiantes.append(promedio)
    print(f"Estudiante {i+1}: {promedio:.2f}")

# Calcular y mostrar el promedio de cada examen (columna)
print("\nPromedio de cada examen:")
for j in range(3):
    suma = 0
    for i in range(num_estudiantes):
        suma += calificaciones[i][j]
    promedio_examen = suma / num_estudiantes
    print(f"Examen {j+1}: {promedio_examen:.2f}")

# Determinar el estudiante con la calificación más alta en el curso
mayor = calificaciones[0][0]
estudiante_mayor = 0
for i in range(num_estudiantes):
    for j in range(3):
        if calificaciones[i][j] > mayor:
            mayor = calificaciones[i][j]
            estudiante_mayor = i

print(f"\nEl estudiante con la calificación más alta es el Estudiante {estudiante_mayor+1} con {mayor}")
