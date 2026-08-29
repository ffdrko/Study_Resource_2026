# Practice 1: Basic Dictionary Operations
# Test your understanding of dictionary methods

print("=== Practice 1: Basic Dictionary Operations ===")

# Create a dictionary
d = {"name": "John", "age": 30, "city": "New York"}

# 1. Test get() method
print("1. Get 'name':", d.get("name"))
print("2. Get 'country' (default):", d.get("country", "Unknown"))
print("3. Get 'country' (no default):", d.get("country"))

# 2. Test keys(), values(), items()
print("\n4. Keys:", list(d.keys()))
print("5. Values:", list(d.values()))
print("6. Items:", list(d.items()))

# 3. Test update()
d.update({"country": "USA", "email": "john@example.com"})
print("\n7. After update:", d)

# 4. Test pop()
popped = d.pop("age")
print("\n8. Popped 'age':", popped)
print("9. After pop:", d)

# 5. Test popitem()
popped_item = d.popitem()
print("\n10. Popped item:", popped_item)
print("11. After popitem:", d)

# 6. Test clear()
d.clear()
print("\n12. After clear:", d)

print("\n=== Practice 1 Complete ===")