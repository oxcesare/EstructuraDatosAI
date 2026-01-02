#Algoritmo que calcule el numero de semanas que una 
#persona debe trabajar para acumular un salario bruto 
#de al menos $2,500
salario_acumulado=0
semanas_trabajadas=0
meta_salario=2500
while salario_acumulado<meta_salario:
    salario_semanal=float(input("Ingrese el salario semanal: "))
    salario_acumulado+=salario_semanal
    semanas_trabajadas+=1
    print("Semanas trabajadas para alcanzar el salario bruto de $2,500:",
           semanas_trabajadas)