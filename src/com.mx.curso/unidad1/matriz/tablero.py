# Tablero de 5x5 representado como una matriz

#Solicitar al usuario que ingrese los valores para cada celda del tablero
tablero = []
for i in range(5):
    fila = []
    for j in range(5):
        valor = input(f"Ingrese el valor para la celda ({i+1},{j+1}): ")
        fila.append(valor)
    tablero.append(fila)

# Imprimir Tablero 
print("Tablero de 5x5:", tablero)

contadorCeros =0
contadorUnos=0

#Imprimir la matriz
for i in range(len(tablero)):
    for j in range(len(tablero[i])):
        if tablero[i][j] == '0':
            contadorCeros +=1
        else:   
             contadorUnos +=1

print("Cantidad de ceros en el tablero: ", contadorCeros)    
print("Cantidad de unos en el tablero: ", contadorUnos)    