# EJERCICIO 8
E = int(input("Número de estudiantes: "))
EX = 3
notas = []
for i in range(E):
    fila = []
    print(f"Estudiante {i}:")
    for j in range(EX):
        while True:
            try:
                n = float(input(f" Calificación examen {j} (0-100): "))
                if 0 <= n <= 100:
                    fila.append(n)
                    break
                else:
                    print("Entre 0 y 100.")
            except ValueError:
                print("Ingresa un número.")
    notas.append(fila)


# Promedio por estudiante (fila)
prom_est = []
for i in range(E):
    prom_est.append(sum(notas[i]) / EX)


# Promedio por examen (columna)
prom_exam = []
for j in range(EX):
    suma = 0
    for i in range(E):
        suma += notas[i][j]
    prom_exam.append(suma / E if E > 0 else 0)


# Estudiante con calificación más alta (mejor nota individual)
max_nota = -1
idx_est_max = -1
for i in range(E):
    for j in range(EX):
        if notas[i][j] > max_nota:
            max_nota = notas[i][j]
            idx_est_max = i


print("\nPromedio por estudiante:")
for i, p in enumerate(prom_est):
    print(f" Estudiante {i}: {p:.2f}")


print("\nPromedio por examen:")
for j, p in enumerate(prom_exam):
    print(f" Examen {j}: {p:.2f}")


print(f"\nCalificación individual más alta: {max_nota:.2f} (Estudiante {idx_est_max})")