d = {
    "Name": "Hasan", "age": 23, "school": "ostad"
}

print("Original dictionary:", d)
print("Type:", type(d))
print("Length:", len(d))
print("Get 'Name':", d["Name"])

# 1. update() - Add or update key-value pairs
d.update({"city": "Dhaka", "country": "Bangladesh"})
print("\nAfter update():", d)

# 2. pop() - Remove and return value for a specific key
popped_value = d.pop("age")
print("\nPopped 'age':", popped_value)
print("After pop('age'):", d)

# 3. popitem() - Remove and return last inserted key-value pair
popped_item = d.popitem()
print("\nPopped item:", popped_item)
print("After popitem():", d)

# 4. clear() - Remove all items from dictionary
d.clear()
print("\nAfter clear():", d)

# Recreate dictionary for further demonstrations
d = {"Name": "Hasan", "age": 23, "school": "ostad", "city": "Dhaka", "country": "Bangladesh"}

# 5. items() - Return view of dictionary's items (key-value pairs)
print("\nItems:", d.items())
for key, value in d.items():
    print(f"  {key}: {value}")

# 6. values() - Return view of dictionary's values
print("\nValues:", d.values())
for value in d.values():
    print(f"  {value}")

# 7. keys() - Return view of dictionary's keys
print("\nKeys:", d.keys())
for key in d.keys():
    print(f"  {key}")

# 8. get() - Return value for key if key is in dictionary, else default
print("\nGet 'Name':", d.get("Name"))
print("Get 'nonexistent' (default):", d.get("nonexistent", "Not found"))
print("Get 'nonexistent' (no default):", d.get("nonexistent"))

# Additional examples
print("\n--- Additional Examples ---")

# Using get() with different scenarios
student = {"name": "Alice", "grade": "A", "major": "Computer Science"}
print("Student info:", student.get("name", "Unknown"))
print("GPA:", student.get("gpa", "Not recorded"))

# Demonstrating that keys(), values(), and items() return views
print("\nType of keys():", type(d.keys()))
print("Type of values():", type(d.values()))
print("Type of items():", type(d.items()))

# Converting views to lists
print("\nKeys as list:", list(d.keys()))
print("Values as list:", list(d.values()))
print("Items as list:", list(d.items()))