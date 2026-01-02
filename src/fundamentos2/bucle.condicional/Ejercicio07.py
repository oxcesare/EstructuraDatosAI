#Algoritmo que solicite depositos mensuales y se detenga
#cuando el saldo supere los $1,000
saldo = 0
while saldo <= 1000:
    deposito = float(input("Ingrese el monto a depositar: "))
    saldo += deposito
    print("El saldo actual es: $", saldo)