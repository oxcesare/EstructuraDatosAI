# principal.py
import logica  # Importamos nuestro otro archivo

def main():
    print("--- Iniciando Programa ---")
    
    # Usamos las funciones del otro archivo
    nombre = "Alex"
    mensaje = logica.saludar_usuario(nombre)
    print(mensaje)
    
    precio = 100
    total = logica.calcular_impuesto(precio)
    print(f"El impuesto de {precio} es: {total}")

# Esta es la "llave de encendido" de Python
if __name__ == "__main__":
    main()