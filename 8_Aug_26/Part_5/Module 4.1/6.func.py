def safe_divide(a, b):
    try:
        result = a / b
        return result
    # custom user friendly messages for each errors (2 except blocks)
    except ZeroDivisionError:
        return "Error: You cannot divide by zero!"
    except TypeError:
        return "Error: Please provide numeric values only."

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "a"))