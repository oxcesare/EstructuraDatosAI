# Ejercicio 8: Calificaciones de Estudiantes con Matriz y Vectores

num_estudiantes = int(input("Número de estudiantes: "))
num_examenes = 3
matriz = []

for i in range(num_estudiantes):
    fila = []
    print(f"Ingresar calificaciones del estudiante {i}:")
    for j in range(num_examenes):
        valor = float(input(f"  Examen {j+1}: "))
        fila.append(valor)
    matriz.append(fila)

# Promedio de cada estudiante
promedios_estudiantes = [sum(fila)/num_examenes for fila in matriz]

# Promedio de cada examen
promedios_examenes = [sum(matriz[i][j] for i in range(num_estudiantes))/num_estudiantes for j in range(num_examenes)]

# Estudiante con mayor calificación en el curso
mejor = max(max(fila) for fila in matriz)

print("Promedio de cada estudiante:", promedios_estudiantes)
print("Promedio de cada examen:", promedios_examenes)
print("Calificación más alta del curso:", mejor)