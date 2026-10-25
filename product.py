class Product:
  def __init__(self, product_id, name, stock, price):
    self.__product_id = product_id
    self.__name = name
    self.__price = price
    self.__stock = stock

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

  def update_stock(self, new_stock):
    self.__stock = new_stock

  def display_information(self):
      print(f"ID: {self.__product_id}, Name: {self.__name}, Quantity: {self.__stock}, Price: ${self.__price}")