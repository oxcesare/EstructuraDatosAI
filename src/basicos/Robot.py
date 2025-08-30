class Robot:
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def saludar(self):
        return f"Hola, soy {self.nombre}!"    
    
    def __str__(self):
        return f"Robot(nombre='{self.nombre}')"
    
mi_robot = Robot("R2D2")
mi_robot.saludar()  # This will return "Hola, soy R2D2!"