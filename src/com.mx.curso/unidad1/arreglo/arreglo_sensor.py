#Simulacion de sensores de un robot

obstaculos = [101,40,10,80,20]

umbral =100

for i in range(len(obstaculos)):
    print(f"\nValor del obstaculo",obstaculos[i])    
    if obstaculos[i] > umbral:
        print("Mensaje de Advertencia, umbral superado")
    else:
        print("Lectura dentro del umbral")
    
