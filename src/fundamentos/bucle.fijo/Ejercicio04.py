#Conteo de Múltiplos en Rango Fijo: Diseñar un algoritmo que cuente cuántos números entre 1 y 150 son múltiplos de 5 O múltiplos de 7.
contador_multiplos = 0
for numero in range(1, 151):
    if numero % 5 == 0 or numero % 7 == 0:
        contador_multiplos += 1
print("Cantidad de números entre 1 y 150 que son múltiplos de 5 o múltiplos de 7:", contador_multiplos)
