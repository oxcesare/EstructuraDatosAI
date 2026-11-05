from Calculadora import Calculadora # Importas la clase

def main():
    # Instanciamos la clase igual que en Java (pero sin 'new')
    mi_calc = Calculadora("Casio")
    
    resultado = mi_calc.sumar(5, 10)
    print(f"La calculadora {mi_calc.marca} dice que el resultado es: {resultado}")

if __name__ == "__main__":
    main()