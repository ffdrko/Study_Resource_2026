# Practice 2: Dictionary Manipulation
# Test your understanding of dictionary modification methods

print("=== Practice 2: Dictionary Manipulation ===")

# Create a dictionary
d = {"Name": "Alice", "age": 25, "city": "London", "country": "UK"}

# 1. Test update() with different scenarios
print("1. Original:", d)
d.update({"age": 26, "email": "alice@example.com"})  # Update existing and add new
print("2. After update:", d)

# 2. Test pop() with different keys
print("\n3. Popping 'city':", d.pop("city"))
print("4. After popping 'city':", d)

# 3. Test popitem() - removes last inserted item
print("\n5. Popping last item:", d.popitem())
print("6. After popitem:", d)

# 4. Test clear()
d.clear()
print("\n7. After clear:", d)

# 5. Test get() with various scenarios
student = {"name": "Bob", "grade": "B", "major": "Math"}
print("\n8. Student name:", student.get("name"))
print("9. Student gpa (default):", student.get("gpa", "Not recorded"))
print("10. Student gpa (no default):", student.get("gpa"))

# 6. Test items() iteration
print("\n11. Iterating through items:")
for key, value in student.items():
    print(f"   {key}: {value}")

# 7. Test keys() and values() conversion
print("\n12. Keys as list:", list(student.keys()))
print("13. Values as list:", list(student.values()))

print("\n=== Practice 2 Complete ===")