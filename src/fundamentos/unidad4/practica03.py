#Calcular el salario bruto y neto de un trabajador considerando la siguiente información:
#El usuario debe ingresar el nombre, las horas trabajadas y el pago por hora
#Sueldo bruto = horas * precio
#Impuestos = bruto * 0.25
#Sueldo neto = bruto - impuestos
#Imprimir el nombre del empleado, el sueldo bruto, los impuestos y el salario neto 
nombre = input("Ingrese el nombre del empleado: ")
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
pago_por_hora = float(input("Ingrese el pago por hora: "))
sueldo_bruto = horas_trabajadas * pago_por_hora
impuestos = sueldo_bruto * 0.25
sueldo_neto = sueldo_bruto - impuestos
print("Empleado:", nombre)
print("Sueldo Bruto: $", sueldo_bruto)
print("Impuestos: $", impuestos)
print("Sueldo Neto: $", sueldo_neto)

