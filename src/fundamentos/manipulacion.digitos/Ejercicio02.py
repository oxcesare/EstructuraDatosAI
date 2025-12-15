#Diseñar un algoritmo que calcule la suma de solamente los dígitos estrictamente mayores a 5 (6, 7, 8, 9) de cualquier número ingresado.
def suma_digitos_mayores_a_cinco(numero):
    suma = 0
    while numero > 0:
        digito = numero % 10
        if digito > 5:
            suma += digito
        numero //= 10  # El operador // realiza una división entera
    return suma
# Solicitar al usuario que ingrese un número entero positivo
numero_usuario = int(input("Ingrese un número entero positivo: "))
if numero_usuario < 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    resultado = suma_digitos_mayores_a_cinco(numero_usuario)
    print("La suma de los dígitos mayores a 5 es:", resultado)