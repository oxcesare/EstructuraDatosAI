#Diseñar un algoritmo que calcule la suma de los dígitos que están en posiciones impares (contando de derecha a izquierda: 1ª, 3ª, 5ª, etc.).
def suma_digitos_posiciones_impares(numero):
    suma = 0
    posicion = 1  # Contador de posición, comenzando desde 1 (derecha a izquierda)
    while numero > 0:
        digito = numero % 10
        print("Digito:", digito, "Posicion:", posicion)
        if posicion % 2 != 0:  # Verificar si la posición es impar
            suma += digito
        numero //= 10  # El operador // realiza una división entera
        posicion += 1  # Incrementar la posición
    return suma
# Solicitar al usuario que ingrese un número entero positivo
numero_usuario = int(input("Ingrese un número entero positivo: "))
if numero_usuario < 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    resultado = suma_digitos_posiciones_impares(numero_usuario)
    print("La suma de los dígitos en posiciones impares es:", resultado)