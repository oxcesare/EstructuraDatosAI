#Se diseñará un algoritmo para calcular el salario mensual de 5 empleados.
#A través de un bucle de repetición, el programa deberá solicitar el nombre, las horas trabajadas y el pago por hora de cada uno de los empleados. Posteriormente, calculará el salario mensual y lo imprimirá en pantalla
#Precio por hora trabajada = $25
#Salario mensual = horas trabajadas x precio 
precio_por_hora = 25
for i in range(5):
    nombre = input("Ingrese el nombre del empleado: ")
    horas_trabajadas = float(input(f"Ingrese las horas trabajadas por {nombre} en el mes: "))
    salario_mensual = horas_trabajadas * precio_por_hora
    print(f"El salario mensual de {nombre} es: ${salario_mensual:.2f}\n")
    
