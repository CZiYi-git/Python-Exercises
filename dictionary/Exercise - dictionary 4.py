# Create a dictionary of menu items and their prices
menu = {
  "Hamburger": 5.99,
  "Cheeseburger": 6.49,
  "Fries": 2.99,
  "Onion Rings": 3.49,
  "Soda": 1.99,
  "Milkshake": 4.99
}

# Print the menu
print("Menu:")
for item, price in menu.items():
  print(f"{item}: ${price:.2f}")

# Create an empty dictionary to hold the order and quantity for each item
order = {}

# Ask the user to enter their order and quantity
while True:
  item = input("Enter an item from the menu (or 'done' to finish): ")
  if item == "done":
    break
  elif item not in menu:
    print(f"Sorry, {item} is not on the menu.")
  else:
    quantity = int(input("Enter the quantity: "))
    order[item] = quantity

# Calculate the total cost of the order
total_cost = 0
print("\nOrder:")
for item, quantity in order.items():
  item_cost = menu[item] * quantity
  # i = i + 1
  total_cost = total_cost+item_cost
  print(f"{quantity} {item} @ ${menu[item]:.2f} each = ${item_cost:.2f}")
print(f"Total cost: ${total_cost:.2f}")

# Hints:
# 1. item variable
# 2. price variable
# 3. stop the while loop by using this statement. (E.g. continue)
# 4. increase total_cost by item_cost
