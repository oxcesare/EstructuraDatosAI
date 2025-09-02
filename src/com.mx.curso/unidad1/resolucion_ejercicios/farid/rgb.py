# Detección de colores en una imagen:
imagen = [[0 ,255, 0], [0, 0, 255], [100, 0, 0],
          [100, 0, 0], [0, 0, 255], [0, 0, 255],
          [0, 255, 0], [100, 0, 0], [100, 0, 0],
          [0, 0, 255], [100, 0, 0,], [0, 0, 255]]
 
rojo = 0
verde = 0
azul = 0
 
 
for i in imagen:
    if i == [0 ,255, 0]:
        verde += 1
    elif i == [0, 0, 255]:
        azul += 1
    else:
        rojo += 1
 
print("\nPixeles Verdes: ", verde)
print("Pixeles Azules: ", azul)
print("Pixeles Rojos : ", rojo)
 