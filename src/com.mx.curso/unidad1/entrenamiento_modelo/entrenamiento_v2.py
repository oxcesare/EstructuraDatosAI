# Importar la librería para trabajar con listas
import sys

# 1. Crear una lista dinámica vacía para el historial de entrenamiento
historial_entrenamiento = []

# 2. Permitir al usuario agregar la precisión de cada época
print("Ingresa las precisiones del modelo. Escribe 'listo' cuando termines.")
while True:
    entrada_usuario = input("Precisión (0.0 - 1.0): ")
    if entrada_usuario.lower() == 'listo':
        break
    try:
        precision = float(entrada_usuario)
        if 0.0 <= precision <= 1.0:
            historial_entrenamiento.append(precision)
        else:
            print("Por favor, ingresa un valor entre 0.0 y 1.0.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")

# 3. Validar si se agregaron datos
if not historial_entrenamiento:
    print("No se ingresaron datos de entrenamiento.")
    sys.exit()

# 4. Mostrar la precisión final del modelo
precision_final = historial_entrenamiento[-1]
print(f"\nHistorial de entrenamiento: {historial_entrenamiento}")
print(f"Precisión final del modelo: {precision_final:.2f}")

# 5. Encontrar y mostrar la precisión más alta
precision_mas_alta = max(historial_entrenamiento)
print(f"La precisión más alta alcanzada fue: {precision_mas_alta:.2f}")