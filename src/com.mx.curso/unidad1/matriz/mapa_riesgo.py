# Mapa de Riesgo para la Navegación de un Vehículo Autónomo

#Crear matriz de 8x8
matriz = [
    [0,1,0,1,1,1,0,1],
    [0,1,0,1,1,1,0,1],
    [0,1,0,1,1,1,0,1],
    [0,1,0,1,2,1,0,1],
    [0,1,0,1,1,1,0,1],
    [0,1,0,1,2,1,0,0],
    [0,1,2,1,1,1,0,0],
    [0,1,0,1,2,1,0,0]
]

# Otra forma de imprimir la matriz 
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print() # Nueva línea después de cada fila

area_riesgo=0
area_precaucion=0


# Imprimir mapa de riesgo
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == 1:
            area_precaucion += 1
        elif matriz[i][j] == 2:
            area_riesgo += 1
    print()  # Nueva línea después de cada fila 

print(f"Área de riesgo (1): {area_riesgo} celdas")
print(f"Área de precaución (2): {area_precaucion} celdas")

# Actualizar el mapa de riesgo
print("\n--- Actualizando el Mapa: Áreas de riesgo a precaución ---")


def actualizar_mapa(matriz):

    area_segura = 0
    area_precaucion = 0
    area_riesgo = 0

    # Recorrer la matriz, actualizar y contar
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 2:
                matriz[i][j] = 1

            # Contar las áreas en la matriz actualizada
            if matriz[i][j] == 0:
                area_segura += 1
            elif matriz[i][j] == 1:
                area_precaucion += 1
            elif matriz[i][j] == 2:
                area_riesgo += 1

    # Retorna un diccionario con los conteos actualizados
    return {
        "segura": area_segura,
        "precaucion": area_precaucion,
        "riesgo": area_riesgo
    }
      
        
# Llamar al método para actualizar y contar
conteo_final = actualizar_mapa(matriz)
print(f"Áreas de precaución (1): {conteo_final['precaucion']}")
print(f"Áreas de alto riesgo (2): {conteo_final['riesgo']}")
print(f"Áreas seguras (0): {conteo_final['segura']}")