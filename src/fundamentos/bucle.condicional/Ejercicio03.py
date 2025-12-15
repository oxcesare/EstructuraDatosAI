#Cálculo de Factorial: Diseñar un algoritmo que calcule el factorial de un número entero positivo ingresado por el usuario (N).
numero = int(input("Ingrese un numero entero positivo para calcular su factorial: "))
factorial = 1
if numero < 0:
    print("El factorial no está definido para números negativos.")
elif numero == 0 or numero == 1:
    print("El factorial de", numero, "es 1.")
else:
    for i in range(2, numero + 1):
        factorial *= i
        print("Iteración", i-1, ": factorial parcial =", factorial)
    print("El factorial de", numero, "es:", factorial)

