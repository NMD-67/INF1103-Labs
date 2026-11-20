from product import Product


class ServiceProduct(Product):
    def __init__(self, product_id, name, stock, price, supplier):
        super().__init__(product_id, name, stock, price, supplier)
        self.__type = "service"

    def display_information(self):
        return super().display_information()

    def get_fulfilment_info(self):
        print("This is a service product and will be delivered digitally!")

    @property
    def type(self):
        return self.__type

    def get_json(self):
        json = super().get_json()
        return json
