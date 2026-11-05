#Algoritmo que simule un inicio de sesion
#permitiendo al usaurio ingresa una contraseña hasta
#un maximo de 3 intentos
contraseña_correcta ="ux"
intentos = 0
max_intentos = 3
while intentos < 3:
    contraseña_ingresa = input("Ingrese la contraseña: ")
    intentos += 1
    if contraseña_ingresa == contraseña_correcta:
        print("Inicio de sesión exitoso")
        break
    else:
        print("Contraseña incorrecta", 3 - intentos)
if intentos == max_intentos:
    print("Se han agotado los intentos, cuenta bloqueada")      

        