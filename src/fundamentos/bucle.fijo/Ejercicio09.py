#Control de Inventario con Precio Condicional: Diseñar un algoritmo para calcular el valor total de una orden de 10 artículos, 
#aplicando un 10% de descuento si el precio unitario es mayor a $50.
valor_total = 0.0
for i in range(10):
    precio_unitario = float(input(f"Ingrese el precio del artículo {i + 1}: "))
    if precio_unitario > 50:
        precio_unitario *= 0.9  # Aplicar 10% de descuento
    valor_total += precio_unitario
print("El valor total de la orden es: $", round(valor_total, 2))
