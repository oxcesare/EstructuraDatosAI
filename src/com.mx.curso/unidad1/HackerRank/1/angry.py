def angry_professor(k, a):
    # Write your code here

    alumnos_puntuales = 0

    for i in range(len(a)):
        if a[i] <= 0:
            alumnos_puntuales += 1

    if alumnos_puntuales >= k:        
        print("NO")        
    else:
        print("YES")        

# llamado a la función
angry_professor(3, [-2, -1, 0, 1, 2])