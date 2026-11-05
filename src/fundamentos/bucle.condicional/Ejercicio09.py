#Validación de Contraseña con Límite de Intentos: Diseñar un algoritmo que simule un inicio de sesión, 
#permitiendo al usuario ingresar una contraseña hasta un máximo de 3 intentos.
contraseña_correcta = "segura123"
intentos = 0
max_intentos = 3
while intentos < max_intentos:
    contraseña_ingresada = input("Ingrese la contraseña: ")
    intentos += 1
    if contraseña_ingresada == contraseña_correcta:
        print("Inicio de sesión exitoso.")
        break
    else:
        print("Contraseña incorrecta. Intento", intentos, "de", max_intentos)
if intentos == max_intentos and contraseña_ingresada != contraseña_correcta:
    print("Se ha alcanzado el número máximo de intentos. Acceso denegado.")