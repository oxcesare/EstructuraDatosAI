#Ejemplo de pila  (LIFO - Last In First Out)
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            raise IndexError("La pila está vacía")

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            raise IndexError("La pila está vacía")

    def tamano(self):
        return len(self.items)
    
# Ejemplo de uso
if __name__ == "__main__":
    pila = Pila()
    pila.apilar(1)
    pila.apilar(2)
    pila.apilar(3)
    print("Tope de la pila:", pila.ver_tope())  
    print("Tamaño de la pila:", pila.tamano())  
    print("Desapilando:", pila.desapilar())     
    print("Tamaño de la pila después de desapilar:", pila.tamano())  