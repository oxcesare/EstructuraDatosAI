#Creacion de una lista
entrenamiento = [1.1,1.2,1.3,1.4,1.5]

print("Entrenamiento inicial :",entrenamiento)

entrenamiento.append(1.7)
print("Entrenamiento actualizado :",entrenamiento)

#Mostrar la precision final 
print("Precision final del modelo:",entrenamiento[-1])

precision_final= entrenamiento[0]

for i in entrenamiento:
    if i > precision_final:
        precision_final=i

print("La mejor precision es:", precision_final)