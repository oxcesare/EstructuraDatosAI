def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here

    # Árbol de manzanas y naranjas:
    apples_counter = 0
    oranges_counter = 0
    auxiliar = 0

    for i in range(len(apples)):
        auxiliar = a + apples[i]
        if auxiliar >= s and auxiliar <= t:
            apples_counter += 1

    for i in range(len(oranges)):
        auxiliar = b + oranges[i]
        if auxiliar >= s and auxiliar <= t:
            oranges_counter += 1

    print(apples_counter)
    print(oranges_counter)

# llamado a la funcion
countApplesAndOranges(7, 10, 4, 12, [2, 3, -4], [3,-2,-4])    