from abc import ABC, abstractmethod
from repository.Product import Product
from typing import List, Optional # Importamos tipos para mayor claridad

class ProductRepository(ABC):
    """
    Define la interfaz para un repositorio de productos,
    especificando las operaciones CRUD básicas que cualquier
    implementación de repositorio debe proporcionar.
    """

    @abstractmethod
    def add_product(self, product: Product) -> None:
        """
        Añade un nuevo producto al repositorio.
        """
        pass

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        """
        Recupera un producto por su ID.
        Retorna el producto si lo encuentra, None en caso contrario.
        """
        pass

    @abstractmethod
    def update_product(self, product: Product) -> None:
        """
        Actualiza un producto existente en el repositorio.
        Se espera que el producto ya exista y su ID sea válido.
        """
        pass

    @abstractmethod
    def delete_product(self, product_id: int) -> None:
        """
        Elimina un producto del repositorio por su ID.
        """
        pass

    @abstractmethod
    def get_all_products(self) -> List[Product]:
        """
        Recupera todos los productos del repositorio.
        """
        pass