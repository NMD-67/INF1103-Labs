import json
from pathlib import Path

INVENTORY_FILE = 'inventory.txt'
inventory_file_path = Path(INVENTORY_FILE)

def get_valid_input():
  product_name = input("\nEnter Product Name: ")
  stock_value = input("Enter Stock Value: ")
  return product_name, stock_value

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
    with open(INVENTORY_FILE) as f:
      value = json.loads(f.read())

  return value

def init_id(inventory):
  next_product_id = 1000
  if len(inventory) > 0:
    next_product_id = inventory[-1]["id"] + 1

  return next_product_id

def calculate_tax(amt):
  tax = 0.1
  return amt * tax

def generate_report(total_units, failed_attempts):
  print("Total units processed: ", total_units)
  print("Number of failed entries: ", failed_attempts)

def get_inventory_size(inventory):
  inventory_count = 0
  for product in inventory:
    inventory_count += int(product["qty"])
  return inventory_count

def save_inventory():
  with open(INVENTORY_FILE, "w") as f:
    f.write(json.dumps(inventory))

def print_product_details(product):
  print(f"{product['id']}, {product['product_name']}, {product['qty']}")

def display_current_orders(inventory):
  print("Current Orders:\n")
  if len(inventory) < 1:
    print("Inventory is Empty...")
  else:
    for product in inventory:
      print_product_details(product)



inventory = load_inventory()
failed_entries = 0
display_current_orders(inventory)
hasQuit = False
while not hasQuit:
  if get_inventory_size(inventory) > 500:
    print("Inventory Full!")
    hasQuit = True
    continue

  new_product = {}
  product_name, stock_value = get_valid_input()

  if (stock_value or product_name) == "quit".lower():
    hasQuit = True
    generate_report(get_inventory_size(inventory), failed_entries)
    save_inventory()
    print(f"Order Saved to {INVENTORY_FILE}")
    continue
  elif not stock_value.isdigit():
    failed_entries += 1
    print("Error: Please input a number!")
    continue
  elif int(stock_value) < 0:
    failed_entries += 1
    print("Error: Negative numbers are invalid!")
    continue
  elif len(product_name) < 1:
    failed_entries += 1
    print("Error: Product Name is Invalid!")
    continue
  else:
    product_id = init_id(inventory=inventory)
    new_product["id"] = product_id
    new_product["product_name"] = product_name
    new_product["qty"] = stock_value
    is_old_product = process_delivery(new_item=new_product, inventory=inventory)
    if is_old_product:
      print(f"\nQuantity add for {new_product['product_name']}:")
    else:
      print("\nNew Order Added:")
    print(f"{new_product['id']}, {new_product['product_name']}, {new_product['qty']}")
    
    # tax_amount = calculate_tax(int(stock_value))
    # print(f"Tax amount for this transaction: ${tax_amount:.2f}")
    continue