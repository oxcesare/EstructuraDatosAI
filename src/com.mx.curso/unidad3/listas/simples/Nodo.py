class Nodo:
    def __init__(self, dato):
        self._dato = dato
        self._siguiente = None

    @property
    def dato(self):
        return self._dato

    @property
    def siguiente(self):
        return self._siguiente

    @siguiente.setter
    def siguiente(self, value):
        self._siguiente = value