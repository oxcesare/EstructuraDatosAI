from Nodo import Nodo


class ListaEnlazada:
    """
    Clase que gestiona la lista simplemente enlazada, incluyendo la cabeza (head).
    """
    def __init__(self):
        self.cabeza = None  # La lista está vacía al inicio

    def insertar_al_inicio(self, nuevo_dato):
        """
        Inserta un nuevo nodo al inicio de la lista. Complejidad: O(1).
        """
        # 1. Crear el nuevo nodo
        nuevo_nodo = Nodo(nuevo_dato)
        
        # 2. Apuntar el 'siguiente' del nuevo nodo a la 'cabeza' actual
        nuevo_nodo.siguiente = self.cabeza
        
        # 3. Mover la 'cabeza' para que apunte al nuevo nodo
        self.cabeza = nuevo_nodo
        print(f"Insertado al inicio: {nuevo_dato}")

    def insertar_al_final(self, nuevo_dato):
        """
        Inserta un nuevo nodo al final de la lista. Complejidad: O(n).
        """
        # 1. Crear el nuevo nodo
        nuevo_nodo = Nodo(nuevo_dato)

        # Caso 1: Si la lista está vacía, el nuevo nodo es la cabeza
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            print(f"Insertado al final (lista vacía): {nuevo_dato}")
            return

        # Caso 2: Si la lista NO está vacía, recorrer hasta el último nodo
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente

        # 3. El último nodo apunta al nuevo nodo
        actual.siguiente = nuevo_nodo
        print(f"Insertado al final: {nuevo_dato}")

    def imprimir_lista(self):
        """
        Imprime todos los elementos de la lista.
        """
        actual = self.cabeza
        elementos = []
        
        # Recorrer hasta que 'actual' sea None (el final de la lista)
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
            
        print("Lista Enlazada:", " -> ".join(elementos) + " -> NULL")

# Ejemplo de uso
if __name__ == "__main__":
    lista = ListaEnlazada()
    
    lista.insertar_al_final(10)
    lista.insertar_al_inicio(5)
    lista.insertar_al_final(15)
    lista.insertar_al_inicio(2)
    
    lista.imprimir_lista()        