#Algoritmo que sume los numeros ingresados por el usuario
#hasta que ingrese un numero fuera del rango[10,50]
suma_total=0
while True:
    numero=int(input("Ingrese un numero entero entre 10 y 50: "))
    if numero<10 or numero>50:
        break
    suma_total+=numero
    print("La suma actual es:",suma_total)