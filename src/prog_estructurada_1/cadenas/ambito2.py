class Contador:
    def __init__(self, nombre):
        # __init__ es el constructor (como el public Contador() en Java)
        self.nombre = nombre
        self.cuenta = 0

    def incrementar(self):
        self.cuenta += 1
        print(f"{self.nombre} tiene una cuenta de: {self.cuenta}")

# Creamos dos instancias diferentes
a = Contador("Instancia A")
b = Contador("Instancia B")

a.incrementar() # Imprime 1
a.incrementar() # Imprime 2
b.incrementar() # Imprime 1 (B es independiente de A)
