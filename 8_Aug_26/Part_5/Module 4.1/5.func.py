def safe_divide(a, b):
    try:
        if b==0 :
            return "Not possible"
        result = a / b
        return result
    except Exception as e:
        return e

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "a"))