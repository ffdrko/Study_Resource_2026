"""
Problem 3: Comprehensions Challenge

Part A (List Comprehension):
Given `numbers = [14, 7, 22, 9, 30, 11, 40, 15]`:
- Create a list `tripled_evens` containing all even numbers multiplied by 3 using a list comprehension.

Part B (Set Comprehension):
Given `words = ["apple", "banana", "apricot", "cherry", "avocado", "blueberry", "almond"]`:
- Create a set `long_word_initials` containing the unique starting letters (in uppercase) of all words that have more than 6 characters using a set comprehension.

Part C (Dictionary Comprehension):
Given `inventory`:
- Create a new dictionary `in_stock_items` containing only products with stock > 0, where the values are formatted as "Available: <count> units" using a dictionary comprehension.
"""

# Part A
numbers = [14, 7, 22, 9, 30, 11, 40, 15]
# Write Part A comprehension below:
triple_evens = [x * 3 for x in numbers if x % 2 == 0]
print(triple_evens)

# Part B
words = ["apple", "banana", "apricot", "cherry", "avocado", "blueberry", "almond"]
# Write Part B comprehension below:
long_word_initials =[x.upper() for x in words if len(x) > 6]
print(long_word_initials)

# Part C
inventory = {
    "Laptop": 15,
    "Mouse": 0,
    "Keyboard": 8,
    "Monitor": 0,
    "Headphones": 12,
    "Webcam": 0
}
# Write Part C comprehension below:
in_stock_items = {item : f"Avaiable : {quant} units" for item, quant in inventory.items() if quant > 0}
print(in_stock_items)