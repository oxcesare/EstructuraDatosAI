import random

alertas = [round(random.random(), 2) for _ in range(10)]

print("Alertas generadas (riesgo original):")
print(alertas)
def seleccion_descendente(lista):
    for i in range(len(lista) - 1):
        maximo = i
        for j in range(i + 1, len(lista)):
            if lista[j] > lista[maximo]:
                maximo = j 
        lista[i], lista[maximo] = lista[maximo], lista[i]


seleccion_descendente(alertas)
print("\nAlertas ordenadas de mayor a menor riesgo:")
print(alertas)