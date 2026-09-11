inventory = 0
failed_entries = 0

hasQuit = False
while not hasQuit:
  if inventory > 500:
    print("Inventory Full!")
    hasQuit = True
    continue
  stock_value = input("Enter Stock Value: ")
  if stock_value == "quit".lower():
    hasQuit = True
    print("Total units processed: ", inventory)
    print("Number of failed entries: ", failed_entries)
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
    inventory += int(stock_value)
    continue