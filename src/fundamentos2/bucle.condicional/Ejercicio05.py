#Algoritmo que acumule numeros enteros ingresados
#por el usuario hasta que la suma supere los 500
suma = 0
while suma <= 500:
    numero = int(input("Ingrese un numero entero: "))
    suma += numero
print("La suma total es:", suma)