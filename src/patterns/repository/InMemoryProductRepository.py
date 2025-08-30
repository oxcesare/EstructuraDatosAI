from repository.Product import Product
from repository.ProductRepository import ProductRepository
from typing import List, Optional

class InMemoryProductRepository(ProductRepository):
    """
    Una implementación de ProductRepository que almacena productos en memoria.
    (No persistente - los datos se pierden al reiniciar la aplicación)
    """
    def __init__(self):
        self._products = {} # Usamos un diccionario para un acceso rápido por ID

    def add_product(self, product: Product) -> None:
        if product.product_id in self._products:
            raise ValueError(f"Product with ID {product.product_id} already exists.")
        self._products[product.product_id] = product
        print(f"Added product: {product}")

    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        return self._products.get(product_id)

    def update_product(self, product: Product) -> None:
        if product.product_id not in self._products:
            raise ValueError(f"Product with ID {product.product_id} not found for update.")
        self._products[product.product_id] = product
        print(f"Updated product: {product}")

    def delete_product(self, product_id: int) -> None:
        if product_id not in self._products:
            raise ValueError(f"Product with ID {product_id} not found for deletion.")
        del self._products[product_id]
        print(f"Deleted product with ID: {product_id}")

    def get_all_products(self) -> List[Product]:
        return list(self._products.values())