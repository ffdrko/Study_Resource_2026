"""
Problem 6: Parallel Processing with zip()

Given four parallel lists representing items bought by a customer:
item_codes = ["ITM-01", "ITM-02", "ITM-03", "ITM-04"]
item_names = ["Wireless Mouse", "Mechanical Keyboard", "USB Hub", "Mousepad"]
quantities = [2, 1, 3, 2]
unit_prices = [25.0, 75.0, 15.0, 10.0]

Tasks:
1. Use `zip()` to iterate through all 4 lists simultaneously in a single loop.
2. For each item, compute the subtotal (quantity * unit_price).
3. Print an itemized receipt line for each product:
   "[<item_code>] <item_name> | Qty: <quantity> | Unit: $<unit_price> | Total: $<subtotal>"
4. Calculate and print the grand total at the end.
"""

item_codes = ["ITM-01", "ITM-02", "ITM-03", "ITM-04"]
item_names = ["Wireless Mouse", "Mechanical Keyboard", "USB Hub", "Mousepad"]
quantities = [2, 1, 3, 2]
unit_prices = [25.0, 75.0, 15.0, 10.0]

# Write your code below:
grand_total = 0

for codes, names, quant, prices in zip(item_codes, item_names, quantities, unit_prices):
   subtotal = quant * prices
   print(f"{codes} {names} | Qty: {quant} | Unit: ${prices} | Total: ${subtotal}")
   grand_total += subtotal

print(f"The grand total is {grand_total}")