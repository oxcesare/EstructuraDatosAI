def angry_professor(k, a):
    attending = "YES"
    b = []

    for time in a:
        if time <= 0:
            b.append(time)

    if len(b) >= k:
        attending = "NO"

    return attending

#Crear una lista de enteros y positivos
list =[-1, -3, 4, 2]
k = 3
print(angry_professor(k, list))  # Output: "YES"
