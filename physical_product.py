from product import Product
from can_be_shipped import CanBeShipped


class PhyscialProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, stock, price, weight, supplier):
        super().__init__(product_id, name, stock, price, supplier)
        self.__weight = weight
        self.__type = "physical"

    def display_information(self):
        return super().display_information(f", Weight: {self.__weight}")

    def get_fulfilment_info(self):
        print("This is a physical product and requires physical shipping!")

    def calculate_shipping_cost(self):
        return self.__weight * 0.67

    @property
    def type(self):
        return self.__type

    def get_json(self):
        json = super().get_json()
        json.update({"weight": self.__weight})
        print(f"json: {json}")
        return json
