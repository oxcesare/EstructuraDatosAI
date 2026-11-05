# Lista con las puntuaciones de importancia
alertas = [0.3, 0.87, 0.45, 0.15, 1, 0.21, 0.78, 0.66, 0.33, 1]

print("Alertas no ordenadas")
print(alertas)

n=len(alertas)

for i in range(n):
    # Suponemos que el elemento i es el mayor
    maximo = i
    for j in range(i+1,n):
        if alertas[j]>alertas[maximo]:
            maximo=j
    # Intercambiar
    temp= alertas[i]
    alertas[i]= alertas[maximo]
    alertas[maximo]=temp

for i in range(len(alertas)):
    print("ID: ", i+1, "riesgo: ", alertas[i])

# Mostrar resultado
print("Alertas ordenadas por importancia (mayor a menor):")
print(alertas)