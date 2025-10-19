import sys
datos = sys.stdin.read().strip().split()

if not datos:
    sys.exit(0)

it= iter(datos)
n = int(next(it))

suma_principal = 0
suma_secundaria = 0

for i in range(n):
    fila = [int(next(it)) for _ in range(n)]
    suma_principal += fila[i]
    suma_secundaria += fila[n - 1 - i]

resultado = abs(suma_principal - suma_secundaria)

print(resultado)

