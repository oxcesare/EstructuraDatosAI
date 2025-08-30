#ejemplo de fibonacci en python
def fibonacci(n):
    # Casos Base: La condición que detiene la recursión
    if n <= 1:
        return n
    # Caso Recursivo: La función se llama a sí misma para resolver subproblemas
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ejemplo de uso
numero = 10
print(f"El número de Fibonacci en la posición {numero} es: {fibonacci(numero)}")