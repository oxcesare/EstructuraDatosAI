# Matriz de una imagen 3x3 en escala de grises
imagen_gris = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print("Matriz de imagen original:")
for fila in imagen_gris:
    print(fila)

# Acceder a un píxel específico (centro)
pixel_central = imagen_gris[1][1]
print(f"\nEl valor del píxel central es: {pixel_central}")

# Modificar un píxel
imagen_gris[0][0] = 5
print("\nMatriz de imagen modificada:")
for fila in imagen_gris:
    print(fila)
