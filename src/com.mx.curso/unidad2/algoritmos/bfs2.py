# Árbol de decisiones para un proceso de ensamblaje automatizado
# Cada nodo representa una acción del brazo robótico
arbol = {
    "Inicio": {
        "Verificar pieza": {
            "Correcta": {
                "Soldar": {
                    "Soldadura OK": {
                        "Empaquetar": {}
                    },
                    "Falla soldadura": {
                        "Descartar pieza": {}
                    }
                }
            },
            "Defectuosa": {
                "Descartar pieza": {}
            }
        }
    }
}

def recorrer_arbol(nodo, indent=0):
    for accion, siguiente in nodo.items():
        print("  " * indent + f"- {accion}")
        recorrer_arbol(siguiente, indent + 1)

# Simulación de la lógica de control del brazo robótico
print("Flujo de decisiones del brazo robótico:\n")
recorrer_arbol(arbol)
