#Generador de Secuencias Impares: Diseñar un algoritmo que imprima los primeros N números impares, donde N es ingresado por el usuario.
N = int(input("Ingrese la cantidad de números impares que desea generar: "))
contador = 0
numero = 1  
print("Los primeros", N, "números impares son:")
while contador < N:
    print(numero)
    numero += 2  
    contador += 1
    