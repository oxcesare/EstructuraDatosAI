# obtener la ruta absoluta del archivo mapa_riesgo.py
import os
ruta_absoluta = os.path.abspath(__file__)
print("Ruta absoluta del archivo mapa_riesgo.py:", ruta_absoluta)

# obtener ruta relativa del archivo mapa_riesgo.py
ruta_relativa = os.path.relpath(__file__)
print("Ruta relativa del archivo mapa_riesgo.py:", ruta_relativa)
