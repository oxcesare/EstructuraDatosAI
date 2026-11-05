
#Arreglo de aves
arr = [1,1,1,2,2,3]

# Contar las aves usando un diccionario
aves = {}
for num in arr:
    aves[num] = aves.get(num, 0) + 1

# Mostrar cuántas veces se repite cada número
for num, count in aves.items():
    print(f'El número {num} se repite {count} veces')

# Obtener el número que más se repite y, en caso de empate, el menor
max_count = max(aves.values())
mayores = [num for num, count in aves.items() if count == max_count]
print('El número que más se repite (menor en empate):', min(mayores))



    