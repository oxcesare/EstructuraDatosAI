#algoritmo que pide 5 números y calcula su promedio 
suma = 0
for i in range(5):
    numero = float(input("Ingrese un número: "))
    suma += numero
promedio = suma / 5
print(f"El promedio de los números ingresados es: {promedio}")