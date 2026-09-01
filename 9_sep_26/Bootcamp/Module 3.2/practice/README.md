# Module 3.2 - Practice Problems

Welcome to the practice section for Module 3.2! 
Work through these problems in their respective Python files inside this `practice/` folder.

---

### **Problem 1: Unique Items & Set Iteration** (`practice/1_unique_iteration.py`)
Given a list of customer order locations that contains duplicates:
```python
locations = ["Dhaka", "Chittagong", "Dhaka", "Sylhet", "Chittagong", "Rajshahi", "Khulna", "Dhaka"]
```
**Task:**
1. Convert the list into a set to eliminate duplicate entries.
2. Iterate through the unique locations and print each city name in uppercase format preceded by `"Location: <CITY>"`.

---

### **Problem 2: Dictionary Iteration & Unpacking** (`practice/2_dict_unpacking.py`)
Given a dictionary of employee names and their monthly salaries:
```python
salaries = {
    "Alvi": 52000,
    "Sadia": 68000,
    "Abir": 45000,
    "Tania": 72000,
    "Rifat": 49000
}
```
**Task:**
1. Iterate over the dictionary using `.items()` with tuple unpacking.
2. Print only the employees who earn **50,000 or more**, in the following format:
   `"<Name> earns $<Salary> per month."`
3. Also print the list of all employee names using `.keys()`.

---

### **Problem 3: Comprehensions Challenge** (`practice/3_comprehensions.py`)
**Part A (List Comprehension):**
Given `numbers = [14, 7, 22, 9, 30, 11, 40, 15]`:
- Create a list `tripled_evens` containing all **even numbers multiplied by 3**.

**Part B (Set Comprehension):**
Given `words = ["apple", "banana", "apricot", "cherry", "avocado", "blueberry", "almond"]`:
- Create a set `long_word_initials` containing the unique starting letters (in uppercase) of all words that have **more than 6 characters**.

**Part C (Dictionary Comprehension):**
Given an inventory dictionary:
```python
inventory = {
    "Laptop": 15,
    "Mouse": 0,
    "Keyboard": 8,
    "Monitor": 0,
    "Headphones": 12,
    "Webcam": 0
}
```
- Create a new dictionary `in_stock_items` containing only products with **stock > 0**, where the values are formatted as `"Available: <count> units"`.

---

### **Problem 4: Deep Nested Data Access** (`practice/4_nested_indexing.py`)
Given the following nested structure:
```python
store_data = [
    "TechZone",
    {"branch_id": 101, "open": True},
    ("Main Street", "Block B", "Level 4"),
    [
        {"category": "Mobile", "items": ["Phone", "Charger", "Case"]},
        {"category": "Audio", "items": [{"name": "Earbuds", "colors": ["Black", "White", "Blue"]}]}
    ]
]
```
**Task:**
Write single-line indexing expressions to retrieve and print:
1. The floor level (`"Level 4"`).
2. The item `"Charger"`.
3. The color `"Blue"`.

---

### **Problem 5: Leaderboard with `enumerate()`** (`practice/5_enumerate_leaderboard.py`)
Given the finishing order of participants in a programming contest:
```python
participants = ["Rahim", "Karim", "Nusrat", "Farhan", "Samiha", "Tanvir"]
```
**Task:**
1. Use `enumerate()` to iterate over the participants with rank numbers starting at `1`.
2. Display a leaderboard with medals for top 3 and rank numbers for the rest:
   - Rank 1: `1. Rahim (Gold Medal)`
   - Rank 2: `2. Karim (Silver Medal)`
   - Rank 3: `3. Nusrat (Bronze Medal)`
   - Rank 4+: `4. Farhan`, `5. Samiha`, etc.

---

### **Problem 6: Parallel Processing with `zip()`** (`practice/6_zip_receipt.py`)
Given four parallel lists representing items bought by a customer:
```python
item_codes = ["ITM-01", "ITM-02", "ITM-03", "ITM-04"]
item_names = ["Wireless Mouse", "Mechanical Keyboard", "USB Hub", "Mousepad"]
quantities = [2, 1, 3, 2]
unit_prices = [25.0, 75.0, 15.0, 10.0]
```
**Task:**
1. Use `zip()` to iterate through all 4 lists simultaneously in a single loop.
2. For each item, compute the subtotal (`quantity * unit_price`).
3. Print an itemized receipt line for each product:
   `"[<item_code>] <item_name> | Qty: <quantity> | Unit: $<unit_price> | Total: $<subtotal>"`
4. Calculate and print the grand total at the end.
