#Sistema de monitoreo con buffer circular y cola de tareas

from collections import deque
import random

# Buffer circular para almacenar las últimas N lecturas de temperatura
class BufferCircular:
    def __init__(self, tamano):
        self.buffer = deque(maxlen=tamano)

    def agregar_lectura(self, valor):
        self.buffer.append(valor)

    def promedio(self):
        if self.buffer:
            return sum(self.buffer) / len(self.buffer)
        return 0

# Cola de tareas (FIFO)
class ColaTareas:
    def __init__(self):
        self.tareas = deque()

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def ejecutar_tarea(self):
        if self.tareas:
            tarea = self.tareas.popleft()
            print(f"Ejecutando tarea: {tarea}")
        else:
            print("No hay tareas en cola.")

# Simulación de uso en mecatrónica
buffer = BufferCircular(5)
cola = ColaTareas()

# Simulamos 7 lecturas de sensor y tareas programadas
for i in range(7):
    lectura = random.randint(20, 30)  # lectura simulada de temperatura
    buffer.agregar_lectura(lectura)
    cola.agregar_tarea(f"Registrar temp: {lectura}°C")

print("\nLecturas almacenadas en buffer circular:", list(buffer.buffer))
print(f"Promedio de temperatura: {buffer.promedio():.2f}°C")

print("\n--- Ejecución de tareas en cola ---")
while cola.tareas:
    cola.ejecutar_tarea()
