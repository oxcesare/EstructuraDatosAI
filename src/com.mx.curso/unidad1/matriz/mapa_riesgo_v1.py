# Mapa de Riesgo

#Crear una matriz de 8x8
matriz = [
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1]]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end="")
    print()     

area_riesgo=0 #2
area_precaucion=0 #1 

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j]==2:
            area_riesgo +=1        
        if matriz[i][j]==1:
            area_precaucion +=1
    print()     

print(f"Area de Riesgo (2): {area_riesgo}")
print(f"Area de Precaucion (1): {area_precaucion}")

# Actualizar la matriz de navegacion
#cambiar todos los 2 por 1

print("Actualizacion de matriz de navegacion")

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j]==2:
            matriz[i][j]=1                  
    print() 

area_riesgo_actulizada=0 #2
area_precaucion_actulizada=0 #1 

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end="")
        if matriz[i][j]==2:
            area_riesgo_actulizada +=1        
        if matriz[i][j]==1:
            area_precaucion_actulizada +=1
    print()   

print(f"Area de Riesgo (2): {area_riesgo_actulizada}")
print(f"Area de Precaucion (1): {area_precaucion_actulizada}")


