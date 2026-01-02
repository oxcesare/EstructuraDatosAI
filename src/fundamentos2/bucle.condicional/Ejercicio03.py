#Calculo de Factorial, de un numero entero positivo 
#ingresado por el usuario
numero = int(input("Introduce un número entero positivo: "))
factorial = 1
if numero <0:
    print("No se puede calcular factorial de numeros negativos")
elif numero ==0 or numero ==1:
    print("El factorial de", numero, "es 1")
else:
    for i in range (2, numero +1):
        factorial *= i
        print("i:", i, "factorial parcial:", factorial)
    print("El factorial de", numero, "es", factorial)