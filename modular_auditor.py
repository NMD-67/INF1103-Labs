inventory = 0
failed_entries = 0

def get_valid_input():
  stock_value = input("Enter Stock Value: ")
  return stock_value

def process_delivery(current_total, new_total):
  return current_total + new_total

def calculate_tax(amt):
  tax = 0.1
  return amt * tax

def generate_report(total_units, failed_attempts):
  print("Total units processed: ", total_units)
  print("Number of failed entries: ", failed_attempts)

hasQuit = False
while not hasQuit:
  if inventory > 500:
    print("Inventory Full!")
    hasQuit = True
    continue
  stock_value = get_valid_input()
  if stock_value == "quit".lower():
    hasQuit = True
    generate_report(inventory, failed_entries)
    continue
  elif not stock_value.isdigit():
    failed_entries += 1
    print("Error: Please input a number!")
    continue
  elif int(stock_value) < 0:
    failed_entries += 1
    print("Error: Negative numbers are invalid!")
    continue
  else:
    inventory = process_delivery(inventory, int(stock_value))
    continue