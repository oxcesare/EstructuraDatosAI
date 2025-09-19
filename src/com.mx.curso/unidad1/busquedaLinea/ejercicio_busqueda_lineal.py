# Ejemplo de búsqueda lineal optimizada

import time
import random
from typing import List, Any, Optional

def busqueda_lineal(arr: List[Any], target: Any) -> bool:
    """
    Realiza una búsqueda lineal en un arreglo.
    
    Args:
        arr: Lista donde buscar
        target: Elemento a buscar
        
    Returns:
        True si encuentra el elemento, False si no
        
    Complejidad: O(n)
    """
    return target in arr  # Más pythónico y optimizado

def busqueda_lineal_con_indice(arr: List[Any], target: Any) -> Optional[int]:
    """
    Realiza una búsqueda lineal y retorna el índice del elemento.
    
    Args:
        arr: Lista donde buscar
        target: Elemento a buscar
        
    Returns:
        Índice del elemento si se encuentra, None si no
    """
    try:
        return arr.index(target)
    except ValueError:
        return None

def busqueda_lineal_manual(arr: List[Any], target: Any) -> bool:
    """
    Implementación manual de búsqueda lineal (para fines educativos).
    """
    for elemento in arr:  # Más pythónico que usar índices
        if elemento == target:
            return True
    return False

def medir_tiempo(func, *args, repeticiones: int = 1000):
    """
    Mide el tiempo promedio de ejecución de una función.
    
    Args:
        func: Función a medir
        *args: Argumentos para la función
        repeticiones: Número de repeticiones para obtener promedio
        
    Returns:
        Tiempo promedio en segundos
    """
    tiempos = []
    
    for _ in range(repeticiones):
        start_time = time.perf_counter()  # Más preciso que time.time()
        func(*args)
        end_time = time.perf_counter()
        tiempos.append(end_time - start_time)
    
    return sum(tiempos) / len(tiempos)

def generar_casos_prueba(n: int):
    """
    Genera diferentes casos de prueba.
    
    Args:
        n: Tamaño del arreglo
        
    Returns:
        Diccionario con diferentes casos de prueba
    """
    arr = list(range(n))
    return {
        'mejor_caso': (arr, 0),          # Primer elemento
        'caso_promedio': (arr, n // 2),   # Elemento en el medio
        'peor_caso': (arr, n + 1),       # Elemento que no existe
        'peor_caso_existe': (arr, n - 1) # Último elemento
    }

def main():
    """Función principal que ejecuta las pruebas."""
    sizes = [100, 1000, 10000, 100000]
    funciones = {
        'Optimizada (in)': busqueda_lineal,
        'Manual': busqueda_lineal_manual,
        'Con índice': lambda arr, target: busqueda_lineal_con_indice(arr, target) is not None
    }
    
    print("=== Comparación de Búsqueda Lineal ===\n")
    
    for n in sizes:
        print(f"📊 Arreglo de {n:,} elementos:")
        casos = generar_casos_prueba(n)
        
        for caso_nombre, (arr, target) in casos.items():
            print(f"\n  🔍 {caso_nombre}:")
            
            for func_nombre, func in funciones.items():
                tiempo_promedio = medir_tiempo(func, arr, target, repeticiones=100)
                print(f"    {func_nombre:15}: {tiempo_promedio*1000:.4f} ms")
        
        print("-" * 50)

def demo_funcionalidad():
    """Demuestra la funcionalidad básica."""
    print("=== Demo de Funcionalidad ===")
    
    # Crear arreglo de prueba
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    
    # Casos de prueba
    casos = [
        (7, "Elemento que existe"),
        (4, "Elemento que no existe"),
        (1, "Primer elemento"),
        (15, "Último elemento")
    ]
    
    for target, descripcion in casos:
        existe = busqueda_lineal(arr, target)
        indice = busqueda_lineal_con_indice(arr, target)
        
        print(f"\n🔍 Buscando {target} ({descripcion}):")
        print(f"   Existe: {existe}")
        print(f"   Índice: {indice}")

if __name__ == "__main__":
    demo_funcionalidad()
    print("\n")
    main()