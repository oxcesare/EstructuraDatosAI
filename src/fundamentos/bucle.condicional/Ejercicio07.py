#Simulación de Depósitos y Meta: Diseñar un algoritmo que solicite depósitos mensuales y se detenga cuando el saldo acumulado supere la meta de $1,000.
saldo_acumulado = 0
meta = 1000
while saldo_acumulado <= meta:
    deposito = float(input("Ingrese el monto del depósito mensual: $"))
    saldo_acumulado += deposito
    print("Saldo acumulado actual: $", saldo_acumulado)