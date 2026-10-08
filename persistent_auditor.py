import json
from pathlib import Path

print("====================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("====================================")

INVENTORY_FILE = 'inventory.json'
inventory_file_path = Path(INVENTORY_FILE)

def process_delivery(new_item, inventory):
  new_product_name = new_item["product_name"]
  product_exists = False
  for product in inventory:
    if product["product_name"] == new_product_name:
      product_exists = True
      old_qty = int(product["qty"])
      product["qty"] = old_qty + int(new_item["qty"])

  if not product_exists:
    inventory.append(new_item)

  return product_exists

def load_inventory():
  value = []
  if inventory_file_path.exists():
    print(f"{INVENTORY_FILE} found, loading inventory...")
    with open(INVENTORY_FILE) as f:
      value = json.loads(f.read())
      print(f"Inventory loaded, {len(value)} items found.\n")

  return value

def init_id(inventory):
  next_product_id = 1000
  if len(inventory) > 0:
    next_product_id = inventory[-1]["id"] + 1

  return next_product_id

def calculate_tax(amt):
  tax = 0.1
  return amt * tax

def quit_handler():
  save_inventory()
  print("Thank you for using the Inventory Management System. Goodbye!")


def get_inventory_size(inventory):
  inventory_count = 0
  for product in inventory:
    inventory_count += int(product["qty"])
  return inventory_count

def save_inventory():
  print(f"Saving inventory to {INVENTORY_FILE}...")
  with open(INVENTORY_FILE, "w") as f:
    f.write(json.dumps(inventory))

def print_product_details(product):
  print(f"ID: {product['id']}, Name: {product['product_name']}, Quantity: {product['qty']}, Price: ${product['price']}")

def display_current_inventory(inventory):
  print("Current Inventory:\n-----------------------------")
  if len(inventory) < 1:
    print("Inventory is Empty...")
  else:
    for product in inventory:
      print_product_details(product)
    print("-----------------------------\n")

def display_current_inventory_handler():
  display_current_inventory(inventory)

def add_new_product_handler():
  new_product = {}
  product_name = input("\nEnter Product Name: ")
  stock_value = input("Enter Stock Quantity: ")
  price_value = input("Enter Price: ")
  if not stock_value.isdigit():
    print("Error: Quantity must be a number!")
    return
  if not price_value.isdigit():
    print("Error: Price must be a number!")
    return
  new_product["id"] = init_id(inventory=inventory)
  new_product["product_name"] = product_name
  new_product["qty"] = stock_value
  new_product["price"] = price_value
  inventory.append(new_product)
  print("\nNew Order Added:")
  print_product_details(new_product)

def update_product_quantity_handler():
  product_id = input("\nEnter Product ID to Update: ")
  if not product_id.isdigit():
    print("Error: Product ID must be a number!")
    return
  for product in inventory:
    if product["id"] == int(product_id):
      new_qty = input(f"Enter New Quantity for {product['product_name']}: ")
      if not new_qty.isdigit():
        print("Error: Quantity must be a number!")
        return
      product["qty"] = new_qty
      print(f"Updated {product['product_name']} to quantity {new_qty}.")
      return
  print(f"Product with ID {product_id} not found.")

def search_product_by_name(inventory, product_name):
  for product in inventory:
    if product["product_name"] == product_name:
      print(f"Product Found\n------------------------------")
      print(f"ID: {product['id']}")
      print(f"Name: {product['product_name']}")
      print(f"Quantity: {product['qty']}")
      print(f"Price: {product['price']}")
      return
  print(f"Product '{product_name}' not found in inventory.")

def search_product_by_name_handler():
  product_name = input("\nEnter Product Name to Search: ")
  search_product_by_name(inventory, product_name)

inventory = load_inventory()
failed_entries = 0
hasQuit = False
options = [
  {"name": "Display All Products", "function": display_current_inventory_handler},
  {"name": "Add New Product", "function": add_new_product_handler},
  {"name": "Update Product Quantity", "function": update_product_quantity_handler},
  {"name": "Search Product by Name", "function": search_product_by_name_handler},
  {"name": "Save Inventory", "function": save_inventory},
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

  # new_product = {}
  # product_name, stock_value = get_valid_input()

  # if (stock_value or product_name) == "quit".lower():
  #   hasQuit = True
  #   generate_report(get_inventory_size(inventory), failed_entries)
  #   save_inventory()
  #   print(f"Order Saved to {INVENTORY_FILE}")
  #   continue
  # elif not stock_value.isdigit():
  #   failed_entries += 1
  #   print("Error: Please input a number!")
  #   continue
  # elif int(stock_value) < 0:
  #   failed_entries += 1
  #   print("Error: Negative numbers are invalid!")
  #   continue
  # elif len(product_name) < 1:
  #   failed_entries += 1
  #   print("Error: Product Name is Invalid!")
  #   continue
  # else:
  #   product_id = init_id(inventory=inventory)
  #   new_product["id"] = product_id
  #   new_product["product_name"] = product_name
  #   new_product["qty"] = stock_value
  #   is_old_product = process_delivery(new_item=new_product, inventory=inventory)
  #   if is_old_product:
  #     print(f"\nQuantity add for {new_product['product_name']}:")
  #   else:
  #     print("\nNew Order Added:")
  #   print(f"{new_product['id']}, {new_product['product_name']}, {new_product['qty']}")
    
  #   # tax_amount = calculate_tax(int(stock_value))
  #   # print(f"Tax amount for this transaction: ${tax_amount:.2f}")
  #   continue