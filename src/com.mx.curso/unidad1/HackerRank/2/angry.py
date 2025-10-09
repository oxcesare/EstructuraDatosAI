def input_entero_positivo(input_text):
    valor = input(input_text)
    while not valor.isdigit():  # se repite hasta que sea un número entero positivo
        print("Error: Ingrese un entero positivo válido.")
        valor = input(input_text)
    return int(valor)

#def input_entero(input_text):
#    while True:
#        valor = input(input_text)
#        try:
#            valor = int(valor)   # se convierte a entero
#            break
#        except ValueError:
#            print("Error: Ingrese un número entero válido.")
#    return valor

#def input_enteros(input_text):
#    while True:
#        valores = input(input_text).split()
#        try:
#            return [int(v) for v in valores]  # convierte todos a int
#        except ValueError:
#            print("Error: Ingrese solo enteros válidos (positivos o negativos).")

def input_enteros_cantidad(input_text, max_valores):
    while True:
        valores = input(input_text).split()
        try:
            numeros = [int(v) for v in valores]   # convierte a enteros
            if len(numeros) > max_valores:        # valida la cantidad
                print(f"Error: Solo puedes ingresar hasta {max_valores} valores.")
            else:
                 return numeros
        except ValueError:
            print("Error: Ingrese solo enteros válidos (positivos o negativos).")


# Generar la funcion que hace el calculo

pruebas = input_entero_positivo("Cantidad de pruebas a realizar: ")

for n in range(pruebas):
    clausulas = input_enteros_cantidad("Ingrese el numero de estudiantes y la cantidad minima para tener la clase: ", 2)
    entrada_estudiantes = input_enteros_cantidad(f"Ingrese la hora de entrada de los {clausulas[0]} estudiantes: ", clausulas[0])

    cont = 0
    for v in entrada_estudiantes:
        if v <= 0:
            cont += 1
    if cont >= clausulas[1]:
        print("YES")
    else:
        print("NO")