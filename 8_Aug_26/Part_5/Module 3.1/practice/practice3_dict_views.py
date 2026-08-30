# Practice 3: Dictionary Views and Type Checking
# Test your understanding of dictionary views and type information

print("=== Practice 3: Dictionary Views and Type Checking ===")

# Create a dictionary
d = {"Name": "Charlie", "age": 35, "city": "Paris", "country": "France"}

# 1. Test type() method
print("1. Type of dictionary:", type(d))
print("2. Type of keys():", type(d.keys()))
print("3. Type of values():", type(d.values()))
print("4. Type of items():", type(d.items()))

# 2. Test view properties
print("\n5. Keys view:", d.keys())
print("6. Values view:", d.values())
print("7. Items view:", d.items())

# 3. Test view conversion to lists
print("\n8. Keys as list:", list(d.keys()))
print("9. Values as list:", list(d.values()))
print("10. Items as list:", list(d.items()))

# 4. Test get() with edge cases
print("\n11. Get existing key 'Name':", d.get("Name"))
print("12. Get non-existing key 'email':", d.get("email"))
print("13. Get non-existing key 'email' with default:", d.get("email", "No email"))

# 5. Test dictionary comprehension (advanced)
print("\n14. Dictionary comprehension - uppercase names:")
uppercase_dict = {k.upper(): v for k, v in d.items()}
print("   Result:", uppercase_dict)

# 6. Test dictionary methods with empty dictionary
empty_dict = {}
print("\n15. Empty dictionary:", empty_dict)
print("16. Empty dict keys:", list(empty_dict.keys()))
print("17. Empty dict values:", list(empty_dict.values()))
print("18. Empty dict items:", list(empty_dict.items()))
print("19. Get from empty dict:", empty_dict.get("test", "Default value"))

print("\n=== Practice 3 Complete ===")