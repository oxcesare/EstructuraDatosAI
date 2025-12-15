#Tabla de Multiplicar Fija: Diseñar un algoritmo que imprima la tabla de multiplicar del número 7 del 1 al 10.
numero = 7
print("Tabla de multiplicar del", numero)
for i in range(1, 11):
    resultado = numero * i
    print("{} x {} = {}".format(numero, i, resultado))
    