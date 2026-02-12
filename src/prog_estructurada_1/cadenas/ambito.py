class Clase:
    def __init__(self):
        self.numero = 10 # Atributo de instancia (como en Java)

    def funcion1(self):
        self.numero += 20 # Usamos 'self' para referirnos al atributo
        print("El numero es:", self.numero)

objeto = Clase()
objeto.funcion1()