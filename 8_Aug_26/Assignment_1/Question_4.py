# Asking the user for item name, price, and quantity
user_item_name = input("Enter the name of the item you have purchased: ")
user_item_price = float(input("Enter the price of the item: TK"))
user_item_quantity = int(input("Enter the quantity of the item: ")) # Using int here as quantity can't be in decimal


# Calculating the total cost
total_cost = user_item_price * user_item_quantity

# Displaying the total cost to the user
print(f"Total bill for {user_item_name} = {total_cost:.2f} Taka") # using :.2f to format the total cost to 2 decimal places