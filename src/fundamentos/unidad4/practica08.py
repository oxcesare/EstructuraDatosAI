#para calcular el promedio de los primeros 50 números pares positivos
suma = 0
for i in range(2, 102, 2):
    suma += i
promedio = suma / 50
print(f"El promedio de los primeros 50 números pares positivos es: {promedio}")
