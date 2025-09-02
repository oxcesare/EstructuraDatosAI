# Reconocimiento de patrones
caracteristicas = [3.5,1.4,0.2]

sum =0

for i in caracteristicas:
    sum += i

print("La suma de las caracteristicas es: ", sum)    

for j in range(len(caracteristicas)):
    caracteristicas[j]= caracteristicas[j]/sum # Normalizacion

print("Las caracteristicas normalizadas son: ", caracteristicas)