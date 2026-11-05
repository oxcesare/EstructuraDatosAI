import pytest
# importar archivo mapa_riesgo.py
import importlib.util
import os

matriz_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'matriz', 'mapa_riesgo.py'))
spec = importlib.util.spec_from_file_location('mapa_riesgo', matriz_path)
if spec is None or spec.loader is None:
    raise ImportError(f"No se pudo encontrar o cargar el módulo mapa_riesgo en {matriz_path}")
mapa_riesgo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mapa_riesgo)

def test_actualizar_mapa():
    matriz = [
        [0,1,0,1,1,1,0,1],
        [0,1,0,1,1,1,0,1],
        [0,1,0,1,1,1,0,1],
        [0,1,0,1,2,1,0,1],
        [0,1,0,1,1,1,0,1],
        [0,1,0,1,2,1,0,0],
        [0,1,2,1,1,1,0,0],
        [0,1,0,1,2,1,0,0]
    ]
    resultado = mapa_riesgo.actualizar_mapa([fila[:] for fila in matriz])
    # Después de actualizar, no debe haber ningún 2 (riesgo)
    assert resultado['riesgo'] == 0
    # El número de áreas de precaución debe aumentar por cada 2 que había
    assert resultado['precaucion'] == 32  # 28 originales + 4 riesgos convertidos
    # El número de áreas seguras debe ser igual
    assert resultado['segura'] == 16
