class Perro:
    def __init__(self,nombre):
        self.nombre = nombre

    def ladar(self):
        print(f"{self.nombre} dice: ¡Guau!")

mi_perro = Perro("firulais")
mi_perro.ladar()        