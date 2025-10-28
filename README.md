# Proyecto Python

Estructura básica de un proyecto en Python.

## Estructura de carpetas
- `src/`: Código fuente del proyecto
- `tests/`: Pruebas del proyecto

## Requisitos
Instala las dependencias con:
```
pip install -r requirements.txt
```

# EstructuraDatosAI

Repositorio educativo con ejercicios y prácticas sobre estructuras de datos y uso de NumPy/Pandas para análisis de datos. Contiene scripts de ejemplo, ejercicios tipo HackerRank y notebooks para prácticas de la materia.

## Descripción
Este proyecto agrupa ejercicios y prácticas usados en la asignatura de Estructuras de Datos. Incluye:
- Carga y procesamiento de datasets (UCI).
- Ejercicios con NumPy y Pandas.
- Problemas tipo HackerRank y soluciones.
- Tests con pytest para algunos módulos.

## Estructura principal (resumen)
- src/com.mx.curso/unidad1/cadenas/         — ejercicios de cadenas (read.py, together.py)
- src/com.mx.curso/unidad1/matriz/numpy/    — prácticas con NumPy (practica_numpy_*)
- src/com.mx.curso/unidad1/HackerRank/      — ejercicios tipo HackerRank
- src/com.mx.curso/unidad1/test/            — tests creados con pytest
- .github/                                  — configuración del proyecto

## Requisitos
- Python 3.8+ (se recomienda usar 3.10+)
- Paquetes principales:
  - numpy
  - pandas
  - pytest
  - ucimlrepo (solo si se usan funciones de fetch_ucirepo)

Instalación rápida:
PowerShell:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
# o instalar paquetes necesarios manualmente
pip install numpy pandas pytest ucimlrepo
```

## Cómo ejecutar scripts de ejemplo
Ejecutar desde la raíz del proyecto (ruta a modo de ejemplo):

PowerShell:
```powershell
python src\com.mx.curso\unidad1\matriz\numpy\practica_numpy_4\heart_disease.py
python src\com.mx.curso\unidad1\cadenas\read.py
python src\com.mx.curso\unidad1\cadenas\together.py
```

Para ejecutar tests con pytest:
```powershell
# desde la raíz del proyecto
pytest src\com.mx.curso\unidad1\test
# o ejecutar un test específico
pytest src\com.mx.curso\unidad1\test\test_mapa_riesgo.py
```

## Notas sobre datasets
- Algunos scripts asumen que los archivos de datos (por ejemplo `iris.data`) están en rutas relativas específicas dentro de `src/...`. Si aparece `FileNotFoundError`, coloca el archivo en la ruta esperada o actualiza la variable de ruta en el script.
- Para `fetch_ucirepo`, el objeto retornado puede variar; los scripts manejan conversiones a DataFrame de forma robusta, pero revisa mensajes en consola si la estructura difiere.

## Buenas prácticas y SonarQube
- Revisar y mantener `__init__.py` en paquetes si se usan importaciones por paquete.
- Eliminar imports no usados y seguir convenciones PEP8.
- Los scripts han sido refactorizados para reducir warnings comunes de SonarQube (nombres, docstrings, simplificación lógica).

## Contribuir
1. Crea una rama con tu cambio: `git checkout -b feature/mi-cambio`
2. Haz commits pequeños y descriptivos.
3. Abre un pull request explicando los cambios.

## Autor y contacto
Repositorio mantenido por César Ricardo Alducin Ruiz (información disponible en el repositorio).

## Licencia
Añadir archivo LICENSE si se desea compartir bajo una licencia específica (recomendado: MIT).
