# Algoritmo SalarioConHorasExtra (Versión Simple sin manejo de errores)

print("--- Cálculo de Salario Mensual con Horas Extra ---")

# 1. Entrada de la constante (Precio por Hora Ordinaria)
# NOTA: Si el usuario ingresa texto aquí, el programa fallará (ValueError)
precio_hora_ordinaria = float(input("Ingresa el precio por hora ORDINARIA: "))

# === 2. BUCLE DE CÁLCULO PARA 5 EMPLEADOS ===
# range(1, 6) itera desde 1 hasta 5
for contador in range(1, 6):
    
    print("\n------------------------------")
    print(f"--- Empleado Número {contador} ---")
    
    # Entrada de Nombre
    nombre = input("Ingresa el nombre del empleado: ")
    
    # Entrada de Horas Semanales
    # NOTA: Si el usuario ingresa texto aquí, el programa fallará (ValueError)
    horas_semana = float(input("Ingresa las horas semanales trabajadas: "))
    
    # 3. ESTRUCTURA DE DECISIÓN (if/else)
    if horas_semana > 40:
        
        # Ruta SÍ (Hay Horas Extra)
        horas_extra = horas_semana - 40
        
        # Cálculo: (40 * PPO + Horas_Extra * PPO * 1.5) * 4
        salario_mensual = (40 * precio_hora_ordinaria + \
                           horas_extra * precio_hora_ordinaria * 1.5) * 4
        
    else:
        
        # Ruta NO (No Hay Horas Extra)
        salario_mensual = (horas_semana * precio_hora_ordinaria) * 4
        
    # 4. SALIDA DE RESULTADOS
    print(f"El Salario Mensual de {nombre} es: ${salario_mensual:,.2f}")
    
# === 5. FIN DEL PROGRAMA ===
print("\n------------------------------")
print("Cálculo finalizado.")