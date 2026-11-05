#Validación de Rango hasta Error: Diseñar un algoritmo que sume números 
# ingresados por el usuario hasta que ingrese un número fuera del rango [10, 50]. (El número que causa la parada NO se suma).
suma_total = 0
while True:
    numero = int(input("Ingrese un número entero entre 10 y 50 (inclusive) para sumar, o un número fuera de este rango para detenerse: "))
    if numero < 10 or numero > 50:
        print("Número fuera de rango. Se detiene la suma.")
        break
    suma_total += numero
    print("Suma parcial actual:", suma_total)