migratory_birds = [1, 1, 2, 2, 3]
tipos = []
conteo_repetidos = []

# Obtener tipos
for i in migratory_birds:
    if i not in tipos:
        tipos.append(i)

# Contar repeticiones
for tipo in tipos:
    contador = 0
    for ave in migratory_birds:
        if ave == tipo:
            contador += 1
    conteo_repetidos.append(contador)

# Tipo más repetido
max_repeticiones = max(conteo_repetidos)
tipos_maximos = []
for i in range(len(tipos)):
    if conteo_repetidos[i] == max_repeticiones:
        tipos_maximos.append(tipos[i])

tipo_pequeño = min(tipos_maximos)

print("Tipos de aves:", tipos)
print("Conteo de repeticiones:", conteo_repetidos)
print("Tipos más comunes:", tipos_maximos)
print("Tipo más pequeño:", tipo_pequeño)