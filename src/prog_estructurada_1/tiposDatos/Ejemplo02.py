# duck Typing

def usar_como_secuencia(seq):
    try:
        primero = seq[0]
        print("Primer elemento:", primero)
    except (TypeError, IndexError):
        print("No se puede indexar o está vacío")

# crear el metod main para probar la funcion
# usar una lista
usar_como_secuencia([1, 2, 3])  
# usar una cadena
usar_como_secuencia("Hola")        