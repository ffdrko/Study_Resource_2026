feet_inches = input("Enter feet and inches: ")
def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    return feet, inches

def convert(feet, inche):
    meters = feet * 0.3048 +inche * 0.0254
    return meters


feets, inches = parse(feet_inches)
print(f"{feets} and {inches}")

result = convert(feets, inches)
print(result)

if result < 1:
    print("Kids is small")
else:
    print("kids is okay to ride.")