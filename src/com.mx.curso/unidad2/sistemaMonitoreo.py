#Ejemplo de sistema simple de monitoreo con recursividad 

#sensor de lectura es una lista de enteros, la funcion contar_altas() es recursiva

#la complejidad del algoritmo 0(n), ya que revisa cada lectura una vez 

# Tipos de datos definidos
sensor_lecturas = [23, 24, 22, 21, 25, 24, 23]  # list of int (temperatura)
umbral_temperatura = 23  # int

# Función recursiva para contar cuántas lecturas están por encima del umbral
def contar_altas(lecturas, umbral, index=0):
    if index >= len(lecturas):  # caso base
        return 0
    # paso recursivo
    if lecturas[index] > umbral:
        return 1 + contar_altas(lecturas, umbral, index + 1)
    else:
        return contar_altas(lecturas, umbral, index + 1)

# Llamada a la función
lecturas_altas = contar_altas(sensor_lecturas, umbral_temperatura)

# Resultado
print(f"Número de lecturas por encima de {umbral_temperatura}°C: {lecturas_altas}")


