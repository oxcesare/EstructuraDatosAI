tarifa = float(input("Ingresa la tarifa por hora"))
#Dame el nombre del trabajador
nombreTrabajador = input("Ingresa el nombre del trabajador")
horasTrabajadas = int(input("Ingresa el numero de horas trabajadas"))

#Definimos salario neto
salarioNeto =0 
salarioBruto= horasTrabajadas*tarifa

#Definimos impuestos
impuestos=0

if(horasTrabajadas<=35):
    salarioBruto = horasTrabajadas*tarifa
else:
     salarioBruto = 35 * tarifa + (horasTrabajadas-35)  * tarifa  

if(salarioBruto<=2000):
    impuestos=0
elif salarioBruto<=2220:
    impuestos = (salarioBruto-2000)*0.20
elif salarioBruto > 2220: 
    impuestos = (salarioBruto-2220)*.030 +(220* 0.20)

salarioNeto = salarioBruto-impuestos

print("Salario del Empleado:", salarioNeto)
         
