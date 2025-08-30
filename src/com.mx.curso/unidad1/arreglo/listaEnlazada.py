#ejemplo lista enlazada
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        
 # Clase para la lista enlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        ultimo = self.cabeza
        while ultimo.siguiente:
            ultimo = ultimo.siguiente
        ultimo.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso
# Crear una lista enlazada y agregar elementos
lista = ListaEnlazada()
lista.insertar(10)
lista.insertar(20)
lista.insertar(30)  
lista.mostrar()  