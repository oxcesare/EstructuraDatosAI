def factorial(n):
    # Caso Base: La condición que detiene la recursión
    if n == 1:
        return 1
    # Caso Recursivo: La función se llama a sí misma con un problema más pequeño
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
numero = 5
print(f"El factorial de {numero} es: {factorial(numero)}")