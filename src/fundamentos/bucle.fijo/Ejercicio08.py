#Validación de Rangos de Edad (10 Personas): Diseñar un algoritmo que solicite la edad de 20 personas 
# y cuente cuántas de ellas se encuentran en el rango de adultez joven (entre 20 y 35 años, ambos inclusive).
contador_adultez_joven = 0
for i in range(10):
    edad = int(input(f"Ingrese la edad de la persona {i + 1}: "))
    if 20 <= edad <= 35:
        contador_adultez_joven += 1
print("Cantidad de personas en el rango de adultez joven (20-35 años):", contador_adultez_joven)
