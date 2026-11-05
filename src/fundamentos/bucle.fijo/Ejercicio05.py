#Búsqueda del Valor Mínimo: Diseñar un algoritmo que solicite la estatura de 8 personas y determine cuál de ellas tiene la estatura más baja.
min_estatura = None
for i in range(8):  
    estatura = float(input(f"Ingrese la estatura de la persona {i + 1} en metros: "))
    if min_estatura is None or estatura < min_estatura:
        min_estatura = estatura
print("La estatura más baja es:", min_estatura, "metros")