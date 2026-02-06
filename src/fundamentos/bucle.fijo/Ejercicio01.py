#Conteo por Rangos de Peso (10 Alumnos): Diseñar un algoritmo que, a partir de la información de 10 alumnos, 
# cuente cuántos caen en rangos predefinidos de peso (ej: menos de 40 kg, entre 40 y 50 kg, etc.).
def contar_por_rango_peso():
    """Pide 10 pesos y devuelve un diccionario con los conteos por rango."""
    contador_menor_40 = 0
    contador_40_50 = 0
    contador_51_60 = 0
    contador_mayor_60 = 0

    for i in range(10):
        peso = float(input("Ingrese el peso del alumno {} en kg: ".format(i + 1)))
        if peso < 40:
            contador_menor_40 += 1
        elif 40 <= peso <= 50:
            contador_40_50 += 1
        elif 51 <= peso <= 60:
            contador_51_60 += 1
        else:
            contador_mayor_60 += 1

    return {
        "menor_40": contador_menor_40,
        "entre_40_50": contador_40_50,
        "entre_51_60": contador_51_60,
        "mayor_60": contador_mayor_60,
    }


def main():
    conteos = contar_por_rango_peso()
    print("Cantidad de alumnos con peso menor a 40 kg:", conteos["menor_40"])
    print("Cantidad de alumnos con peso entre 40 y 50 kg:", conteos["entre_40_50"])
    print("Cantidad de alumnos con peso entre 51 y 60 kg:", conteos["entre_51_60"])
    print("Cantidad de alumnos con peso mayor a 60 kg:", conteos["mayor_60"])


if __name__ == "__main__":
    main()
