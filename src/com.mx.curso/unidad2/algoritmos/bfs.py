#Ejemplo practico: Robot autonomo que busca el mejor
#camino en una red de nodos (grafos)

from collections import deque

# Grafo representando zonas de una planta industrial
grafo = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

def bfs_camino(grafo, inicio, destino):
    cola = deque([[inicio]])
    visitados = set()

    while cola:
        camino = cola.popleft()
        nodo = camino[-1]

        if nodo == destino:
            return camino

        if nodo not in visitados:
            for vecino in grafo[nodo]:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)
            visitados.add(nodo)
    return None

# Simulación: el robot va de A a F
camino_optimo = bfs_camino(grafo, "A", "F")
print("Ruta óptima del robot:", " → ".join(camino_optimo))
