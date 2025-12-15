#Conteo de Positivos, Negativos y Ceros: Diseñar un algoritmo que solicite $X$ cantidad de números 
# (definida por el usuario) y cuente cuántos son positivos, cuántos negativos y cuántos cero.
cantidad_numeros = int(input("Ingrese la cantidad de números que desea evaluar: "))
contador_positivos = 0
contador_negativos = 0  
contador_ceros = 0
for i in range(cantidad_numeros):
    numero = float(input("Ingrese el número {}: ".format(i + 1)))
    if numero > 0:
        contador_positivos += 1
    elif numero < 0:
        contador_negativos += 1
    else:
        contador_ceros += 1
print("Cantidad de números positivos:", contador_positivos)
print("Cantidad de números negativos:", contador_negativos)
print("Cantidad de ceros:", contador_ceros)