#Acumulación de Salario Condicional (Meta $2,500): Diseñar un algoritmo que calcule el 
# número de semanas que una persona debe trabajar para acumular un salario bruto de al menos $2,500, solicitando el salario semanal.
salario_acumulado = 0
meta_salario = 2500
semanas_trabajadas = 0
while salario_acumulado < meta_salario:
    salario_semanal = float(input("Ingrese el salario semanal: $"))
    salario_acumulado += salario_semanal
    semanas_trabajadas += 1
    print("Salario acumulado actual: $", salario_acumulado)
print("Número de semanas trabajadas para alcanzar la meta:", semanas_trabajadas)
print("Meta de salario bruto de $2,500 alcanzada.")