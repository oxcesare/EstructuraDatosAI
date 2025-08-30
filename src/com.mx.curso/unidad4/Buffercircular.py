class CircularBuffer:
    def __init__(self, size):
        self.buffer = [None] * size  # espacio fijo
        self.size = size
        self.start = 0
        self.end = 0
        self.full = False

    def append(self, data):
        self.buffer[self.end] = data
        self.end = (self.end + 1) % self.size

        if self.full:
            self.start = (self.start + 1) % self.size
        elif self.end == self.start:
            self.full = True

    def read_all(self):
        items = []
        i = self.start
        if not self.full and self.start == self.end:
            return []  # vacío
        while True:
            items.append(self.buffer[i])
            if i == self.end - 1 and not self.full:
                break
            i = (i + 1) % self.size
            if i == self.end and self.full:
                break
        return items

    def __repr__(self):
        return f"CircularBuffer({self.read_all()})"
# Crear buffer de tamaño 5
cb = CircularBuffer(5)

# Agregar elementos
for i in range(1, 8):
    cb.append(i)
    print(cb)

# Resultado:
# CircularBuffer([1])
# CircularBuffer([1, 2])
# CircularBuffer([1, 2, 3])
# CircularBuffer([1, 2, 3, 4])
# CircularBuffer([1, 2, 3, 4, 5])
# CircularBuffer([2, 3, 4, 5, 6])  <- 1 fue sobreescrito
# CircularBuffer([3, 4, 5, 6, 7])  <- 2 fue sobreescrito