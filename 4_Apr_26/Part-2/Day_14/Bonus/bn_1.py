import func
feet_inches = input("Enter feet and inches: ")


parsed = func.parse(feet_inches)

result = func.convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")