import time
# Entrenamiento de una red neuronal 

entrada = [1,2,5]

# Matriz Pesos 3 x 2
# 
pesos = [
    [4,1,5,6],
    [4,1,5,6],
    [3,1,1,6],
]

salida = [0,0,0,0]
start_time = time.time()

for j in range(len(pesos[0])):
    for i in range(len(entrada)):
        salida[j] += entrada[i] * pesos[i][j]

end_time = time.time()


print("Incio :", start_time)
print("Tiempos :", end_time-start_time)
print("Vector Entrada", entrada)
print("Matriz Pesos", pesos)
print("Vector Salida", salida)