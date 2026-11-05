#Algoritmo que calcule la suma de todos los numeros 
#Enteros del 1 al 100 que son divisibles entre 3 y ademas,impares
suma=0
for numero in range(1,101):
    if numero % 3== 0 and numero % 2 !=0:
        suma+=numero
print("La suma de los números enteros del 1 al 100 que " \
          "son divisibles entre 3 y además impares es:", suma)