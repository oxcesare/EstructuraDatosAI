#Promedio Condicional de Edades (15 Adultos): Diseñar un algoritmo que calcule el promedio de edad de solamente los adultos (= 18 años) de un grupo de 15 personas.
suma_edades_adultos = 0
contador_adultos = 0
for i in range(15):
    edad = int(input(f"Ingrese la edad de la persona {i + 1}: "))
    if edad >= 18:
        suma_edades_adultos += edad
        contador_adultos += 1
if contador_adultos > 0:
    promedio_adultos = suma_edades_adultos / contador_adultos
    print("El promedio de edad de los adultos es:", promedio_adultos)
else:
    print("No se ingresaron edades de adultos.")