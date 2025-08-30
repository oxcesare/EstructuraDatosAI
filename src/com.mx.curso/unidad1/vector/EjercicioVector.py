# Vector de características: [altura, peso, edad]
caracteristicas = [1.75, 70, 30]
print(f"Vector original: {caracteristicas}")

# Acceder a un elemento (peso)
peso = caracteristicas[1]
print(f"El peso es: {peso}")

# Modificar un elemento
caracteristicas[2] = 35
print(f"Vector modificado: {caracteristicas}")

# Calcular la media
media = sum(caracteristicas) / len(caracteristicas)
print(f"La media de las características es: {media:.2f}")

