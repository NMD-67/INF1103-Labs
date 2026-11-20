import json
from product import Product


class Inventory:
    def __init__(self):
        self.__product_list: list[Product] = []

    def add_product(self, new_product: Product) -> None:
        self.__product_list.append(new_product)

    def remove_product(self, product_id: int) -> bool:
        for index, product in enumerate(self.__product_list):
            if product.product_id == product_id:
                self.__product_list.pop(index)
                return True
        return False

    def search_product(self, product_id: int) -> Product | None:
        for product in self.__product_list:
            if product.product_id == int(product_id):
                return product
        return None

    def search_product_by_name(self, product_name: str) -> Product | None:
        for product in self.__product_list:
            if product.name.lower() == product_name.lower():
                return product
        return None

    def display_all(self) -> None:
        print("Current Inventory:\n-----------------------------")
        if len(self.__product_list) < 1:
            print("Inventory is Empty...")
        else:
            for product in self.__product_list:
                product.display_information()
                product.get_fulfilment_info()
            print("-----------------------------\n")

    def get_next_product_id(self) -> int:
        if len(self.__product_list) == 0:
            return 1000
        return self.__product_list[-1].product_id + 1

    def get_inventory_size(self) -> int:
        return len(self.__product_list)

    def save_inventory(self, INVENTORY_FILE: str) -> None:
        print(f"Saving inventory to {INVENTORY_FILE}...")
        saving_list = []
        for product in self.__product_list:
            saving_list.append(product.get_json())
        with open(INVENTORY_FILE, "w") as f:
            f.write(json.dumps(saving_list))
