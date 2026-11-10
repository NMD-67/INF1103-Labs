from abc import ABC, abstractmethod
from supplier import Supplier


class Product(ABC):
    def __init__(
        self, product_id: int, name: str, stock: int, price: float, supplier: Supplier
    ):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.supplier: Supplier = supplier

    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def stock(self):
        return self.__stock

    @property
    @abstractmethod
    def type(self):
        pass

    def update_stock(self, new_stock):
        self.__stock = new_stock

    def display_information(self, additional_stats=None):
        print(
            f"ID: {self.__product_id}, Name: {self.__name}, Quantity: {self.__stock}, Price: ${self.__price}"
            + additional_stats
        )

    @abstractmethod
    def get_fulfilment_info(self):
        pass

    def get_json(self):
        return {
            "product_id": self.product_id,
            "product_name": self.name,
            "qty": self.stock,
            "price": self.price,
            "type": self.type,
        }
