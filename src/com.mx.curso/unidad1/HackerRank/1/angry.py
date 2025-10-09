def angryProfessor(k, a):
    # Write your code here
    
    umbral = 3
    alumnos_puntuales = 0
    alumnos_impuntuales = 0

    for i in range(len(a)):
        if a[i] <= 0:
            alumnos_puntuales += 1
        elif a[i] > 0:
            alumnos_impuntuales += 1

    if alumnos_puntuales >= k:        
        print(f"NO")        
    elif alumnos_puntuales < k:
        print(f"YES")        

# llamado a la fucnion
angryProfessor(3, [-2, -1, 0, 1, 2])
