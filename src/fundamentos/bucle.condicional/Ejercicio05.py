#Suma con Tope por Valor (Límite 500): Diseñar un algoritmo que acumule números enteros 
# ingresados por el usuario hasta que la suma total supere los 500. (El número que causa la parada SÍ se suma).
suma_total = 0
while suma_total <= 500:
    numero = int(input("Ingrese un número entero para sumar (la suma se detendrá cuando supere 500): "))
    suma_total += numero
    print("Suma parcial actual:", suma_total)