def count_apples_and_oranges(s, t, a, b, apples, oranges):
    cont_apples = 0
    for i in range(len(apples)):
        aux = a + apples[i]
        if s <= aux <= t:
            cont_apples += 1

    cont_oranges = 0
    for i in range(len(oranges)):
        aux = b + oranges[i]
        if s <= aux <= t:
            cont_oranges += 1

    print(cont_apples)
    print(cont_oranges)


# Crear una lista de manzanas
manzanas = [-2, 2, 1]

# Crear una lista de naranjas
naranjas = [5, -6]

s=7
t=11
a=5
b=15
count_apples_and_oranges(s, t, a, b, manzanas, naranjas)
