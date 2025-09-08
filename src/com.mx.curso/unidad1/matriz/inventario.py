# Inventario de Productos

#ProductoA -- 1700
#ProductoB -- 1101
#ProductoC -- 1703
#ProductoD -- 1102
 
matriz = [
    [1101, 11,9.77],
    [1477, 18,1.77],
    [1703, 9,2.77],
    [1477, 7,3.77],
]


#Imprimir la matriz
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print() # Nueva línea después de cada fila

#Motrar los datos de un producto en especifico
producto = matriz[0]
if  matriz[0][1] >0:
    valor = matriz[0][1]*matriz[0][2]
    print("Datos de un producto en especifico ", producto)
    print("Valor total de un producto ", valor)
    #Actualizamos la matriz con el producto que se vendio
    matriz[0][1]= 0


    #Imprimir la matriz después de actualizar un dato
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print() # Nueva línea después de cada fila
else:
    print("No se puede realizar la operación, no se cuenta con inventario")    





