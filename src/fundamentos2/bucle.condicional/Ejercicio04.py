#Algoritmo que imprima los primeros N numeros impares, 
#Donde N es ingresado por el usuario 
N = int(input("Ingrese la cantidad de numeros impares " \
"que desea imprimir: "))
contador =0
numero =1
print("Los primeros",N, "numeros impares son: ")
while contador < N:
    print(numero)
    numero +=2
    contador +=1