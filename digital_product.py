from product import Product


class DigitalProduct(Product):
    def __init__(self, product_id, name, stock, price, size, supplier):
        super().__init__(product_id, name, stock, price, supplier)
        self.__download_size = size
        self.__type = "digital"

    @property
    def size(self):
        return self.__download_size

    def display_information(self):
        return super().display_information(f", Download Size: {self.__download_size}")

    def get_fulfilment_info(self):
        print("This is a digital product and will be delivered digitally!")

    @property
    def type(self):
        return self.__type

    def get_json(self):
        json = super().get_json()
        json.update({"download_size": self.__download_size})
        print(f"Json: {json}")
        return json
