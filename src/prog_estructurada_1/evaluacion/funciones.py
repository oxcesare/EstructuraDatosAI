def leer_tres_numeros():
    """
    Lee tres números flotantes del usuario y los regresa como una tupla.
    No valida errores para mantenerlo simple.
    """
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    c = float(input("Ingresa el tercer número: "))
    return a, b, c


def calcular_promedio(a, b, c):
    """
    Regresa el promedio de tres números.
    """
    return (a + b + c) / 3


def mayor_de_tres(a, b, c):
    """
    Regresa el mayor de tres números.
    """
    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c
    return mayor


def main():
    """
    Punto de entrada del programa:
    - Llama a las funciones
    - Orquesta el flujo
    - Presenta los resultados
    """
    print("=== Cálculos con 3 números ===")
    a, b, c = leer_tres_numeros()

    promedio = calcular_promedio(a, b, c)
    mayor = mayor_de_tres(a, b, c)

    print(f"\nResultados:")
    print(f"  Números: {a}, {b}, {c}")
    print(f"  Promedio: {promedio}")
    print(f"  Mayor: {mayor}")


# Convención para ejecutar solo cuando el archivo es el principal
if __name__ == "__main__":
    main()
