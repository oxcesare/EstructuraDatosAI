#crear un diccionario con 3 llaves y 3 valores cada una
mi_diccionario = {
    "nombre": ["Ana", "Luis", "Carlos"],
    "edad": [28, 34, 29],
    "ciudad": ["Madrid", "Barcelona", "Valencia"]
}

#Iterar sobre el diccionario e imprimir cada llave y su valor
for llave, valor in mi_diccionario.items():
    print(f"{llave}: {valor}")
    