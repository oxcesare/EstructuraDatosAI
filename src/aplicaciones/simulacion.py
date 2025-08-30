#Simulacion de FIFO, prioridad y PID

from collections import deque
import heapq
import random
import time

# 1. FIFO (cola) para simular tareas en PLC
cola_tareas = deque(["Verificar sensor", "Activar motor", "Enviar señal", "Esperar"])

print("Simulación FIFO (orden de atención):")
while cola_tareas:
    tarea = cola_tareas.popleft()
    print(f"Ejecutando: {tarea}")
time.sleep(1)

# 2. Cola de prioridad (sensor crítico = menor valor => mayor prioridad)
sensores = []
heapq.heappush(sensores, (2, "Sensor presión"))
heapq.heappush(sensores, (1, "Sensor temperatura crítica"))
heapq.heappush(sensores, (3, "Sensor humedad"))

print("\nAtención por prioridad de sensores:")
while sensores:
    prioridad, sensor = heapq.heappop(sensores)
    print(f"Atendiendo: {sensor} (prioridad {prioridad})")
time.sleep(1)

# 3. Control PID (historial de errores simulados)
class PID:
    def __init__(self, Kp, Ki, Kd):
        self.Kp, self.Ki, self.Kd = Kp, Ki, Kd
        self.historial_error = deque(maxlen=2)  # e(t-1), e(t-2)
        self.integral = 0

    def calcular(self, error):
        self.historial_error.appendleft(error)
        self.integral += error
        derivada = 0
        if len(self.historial_error) > 1:
            derivada = self.historial_error[0] - self.historial_error[1]
        salida = self.Kp * error + self.Ki * self.integral + self.Kd * derivada
        return salida

pid = PID(1.0, 0.1, 0.5)
print("\nControl PID (simulado):")
for lectura in [5, 4, 3, 2, 1]:
    error = 0 - lectura  # referencia deseada es 0
    salida = pid.calcular(error)
    print(f"Error: {error}, Salida PID: {salida:.2f}")
time.sleep(1)

# 4. Registro de eventos del sistema
log_eventos = []

def registrar_evento(tipo, descripcion):
    timestamp = time.strftime("%H:%M:%S")
    log_eventos.append(f"[{timestamp}] {tipo.upper()}: {descripcion}")

registrar_evento("info", "Motor activado")
registrar_evento("warning", "Alta temperatura detectada")
registrar_evento("error", "Fallo en sensor de presión")

print("\nLog del sistema:")
for evento in log_eventos:
    print(evento)
