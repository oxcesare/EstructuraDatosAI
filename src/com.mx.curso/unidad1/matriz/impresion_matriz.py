#matriz 3 x 3

matriz = [
    [0,1,0],
    [0,1,22],
    [1,2,3]];

for fila in matriz:
    print(fila)

valorEncontrado = matriz[2][2]
matriz[0][0]=100

nuevoValor = matriz[0][0]

print(valorEncontrado)
print(matriz)
