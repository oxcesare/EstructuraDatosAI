#determinar si la suma de cualquier par de tres números es igual al tercero
def suma_igual_tercero(a, b, c):
    return a + b == c or a + c == b or b + c == a
#ejemplo de uso
resultado = suma_igual_tercero(3, 5, 8)
print(f"La suma de algún par de números es igual al tercero: {resultado}")
