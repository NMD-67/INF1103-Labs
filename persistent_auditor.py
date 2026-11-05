import json
from pathlib import Path
from product import Product
from inventory import Inventory
from physical_product import PhyscialProduct
from digital_product import DigitalProduct

INVENTORY_FILE = 'inventory.json'
inventory_file_path = Path(INVENTORY_FILE)

print("====================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("====================================")

def load_inventory():
  product_list = []
  file_value = []
  if inventory_file_path.exists():
    print(f"{INVENTORY_FILE} found, loading inventory...")
    with open(INVENTORY_FILE) as f:
      content = f.read()
      if content != "":
        file_value = json.loads(content)
        print(f"Inventory loaded, {len(file_value)} items found.\n")

  for product in file_value:
    id = product["product_id"]
    name = product["product_name"]
    qty = product["qty"]
    price = product["price"]
    product_type = product["type"]
    new_product = PhyscialProduct(id, name, qty, price, product["weight"]) if product_type == "physical" else DigitalProduct(id, name, qty, price, product["download_size"])
    product_list.append(new_product)

  return product_list

def quit_handler():
  inventory.save_inventory(INVENTORY_FILE)
  print("Thank you for using the Inventory Management System. Goodbye!")

def display_current_inventory_handler():
  inventory.display_all()

def add_new_product_handler():
  new_product = {}
  product_name = input("\nEnter Product Name: ")
  stock_value = input("Enter Stock Quantity: ")
  price_value = input("Enter Price: ")
  product_type = input("Enter Product Type (Physical [p]/ Digital [d]): ")
  if not stock_value.isdigit():
    print("Error: Quantity must be a number!")
    return
  if not price_value.isdigit():
    print("Error: Price must be a number!")
    return
  if not product_type == "p" and not product_type == "d":
    print("Error: Product Type must be either p or d")
    return
  prompt = "weight" if product_type == "p" else "download size"
  attr = input(f"Enter the product's {prompt}: ")
  id = inventory.get_next_product_id()
  new_product = PhyscialProduct(id, product_name, stock_value, price_value, attr) if product_type == "p" else DigitalProduct(id, product_name, stock_value, price_value, attr)
  inventory.add_product(new_product)
  print("\nNew Order Added:")
  new_product.display_information()

def update_product_quantity_handler():
  product_id = input("\nEnter Product ID to Update: ")
  if not product_id.isdigit():
    print("Error: Product ID must be a number!")
    return
  product = inventory.search_product(product_id)
  if product is not None:
    new_qty = input(f"Enter New Quantity for {product.name}: ")
    if not new_qty.isdigit():
      print("Error: Quantity must be a number!")
      return
    product.update_stock(new_qty)
    print(f"Updated {product.name} to quantity {new_qty}.")
    return
  print(f"Product with ID {product_id} not found.")

def search_product_by_name(product_name):
  search_result = inventory.search_product_by_name(product_name)
  if search_result is None:
    return print(f"Product '{product_name}' not found in inventory.")
  search_result.display_information()

def search_product_by_name_handler():
  product_name = input("\nEnter Product Name to Search: ")
  search_product_by_name(product_name)

def save_inventory_handler():
  inventory.save_inventory(INVENTORY_FILE)

# inventory = load_inventory()
inventory = Inventory()
for product in load_inventory():
  inventory.add_product(product)
failed_entries = 0
hasQuit = False
options = [
  {"name": "Display All Products", "function": display_current_inventory_handler},
  {"name": "Add New Product", "function": add_new_product_handler},
  {"name": "Update Product Quantity", "function": update_product_quantity_handler},
  {"name": "Search Product by Name", "function": search_product_by_name_handler},
  {"name": "Save Inventory", "function": save_inventory_handler},
  {"name": "Quit", "function": quit_handler}
]
while not hasQuit:
  print("-------------MENU----------------")
  for option in options:
    print(f"{options.index(option) + 1}. {option['name']}")
  print("---------------------------------\n")
  user_choice = input("Select an option (1-6): ")

  # Check if the user input is a valid option
  if not user_choice.isdigit() or int(user_choice) < 1 or int(user_choice) > len(options):
    print("Invalid option. Please select a valid option (1-6).")
    continue

  selected_option = options[int(user_choice) - 1]
  selected_option["function"]()

  if selected_option["name"] == "Quit":
    hasQuit = True