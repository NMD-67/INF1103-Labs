import json

class Inventory:
  def __init__(self):
    self.__product_list = []

  def add_product(self, new_product):
    self.__product_list.append(new_product)

  def search_product(self, product_id):
    for product in self.__product_list:
      if product.product_id == int(product_id):
        return product
    return None

  def search_product_by_name(self, product_name):
    for product in self.__product_list:
      if product.name == product_name:
        return product
    return None

  def display_all(self):
    print("Current Inventory:\n-----------------------------")
    if len(self.__product_list) < 1:
      print("Inventory is Empty...")
    else:
      for product in self.__product_list:
        product.display_information()
      print("-----------------------------\n")

  def get_next_product_id(self):
    if len(self.__product_list) == 0:
      return 1000
    return self.__product_list[-1].product_id + 1

  def get_inventory_size(self):
    return len(self.__product_list)

  def save_inventory(self, INVENTORY_FILE):
    print(f"Saving inventory to {INVENTORY_FILE}...")
    saving_list = []
    for product in self.__product_list:
      saving_list.append({
        "product_id": product.product_id,
        "product_name": product.name,
        "qty": product.stock,
        "price": product.price
      })
    with open(INVENTORY_FILE, "w") as f:
      f.write(json.dumps(saving_list))
