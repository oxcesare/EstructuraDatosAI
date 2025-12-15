#Conteo de Calificaciones Aprobatorias: Diseñar un algoritmo que procese 12 calificaciones y calcule el promedio de solamente las aprobatorias (= 70), y el total de aprobados.
suma_calificaciones_aprobatorias = 0
contador_aprobados = 0
for i in range(5):
    calificacion = float(input(f"Ingrese la calificación {i + 1}: "))
    if calificacion >= 70:
        suma_calificaciones_aprobatorias += calificacion
        contador_aprobados += 1
if contador_aprobados > 0:
    promedio_aprobatorias = suma_calificaciones_aprobatorias / contador_aprobados
    print("El promedio de las calificaciones aprobatorias es:", promedio_aprobatorias)
    print("El total de calificaciones aprobatorias es:", contador_aprobados)