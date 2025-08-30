from repository.ProductRepository import ProductRepository
from repository.Product import Product
from repository.InMemoryProductRepository import InMemoryProductRepository

# --- Uso del repositorio ---
if __name__ == "__main__":
    repository: ProductRepository = InMemoryProductRepository() # Especificamos el tipo de la interfaz

    # Añadir productos
    product1 = Product(product_id=1, name="Laptop", price=1200.50)
    product2 = Product(product_id=2, name="Mouse", price=25.99)
    product3 = Product(product_id=3, name="Keyboard", price=75.00)

    repository.add_product(product1)
    repository.add_product(product2)
    repository.add_product(product3)

    print("\n--- Todos los productos después de añadir ---")
    for p in repository.get_all_products():
        print(p)

    # Obtener un producto
    found_product = repository.get_product_by_id(2)
    print(f"\nProducto encontrado por ID 2: {found_product}")

    not_found_product = repository.get_product_by_id(99)
    print(f"Producto encontrado por ID 99: {not_found_product}") # Debería ser None

    # Actualizar un producto
    product1.price = 1150.00 # Actualizamos el precio
    repository.update_product(product1)
    print(f"Producto 1 después de actualizar: {repository.get_product_by_id(1)}")

    # Intentar actualizar un producto que no existe
    # try:
    #     repository.update_product(Product(id=4, name="NonExistent", price=10))
    # except ValueError as e:
    #     print(f"\nError al intentar actualizar: {e}")

    # Eliminar un producto
    repository.delete_product(3)

    print("\n--- Todos los productos después de eliminar ---")
    for p in repository.get_all_products():
        print(p)

    # Intentar eliminar un producto que no existe
    # try:
    #     repository.delete_product(99)
    # except ValueError as e:
    #     print(f"\nError al intentar eliminar: {e}")

