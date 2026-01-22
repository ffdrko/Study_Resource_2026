from functions import parse, convert

feet_inches = input("Enter feet and inches: ")

feet_tuple = parse(feet_inches)
print(feet_tuple)

result = convert(feet_tuple[0], feet_tuple[1])
print(result)

if result < 1:
    print("Kids is small")
else:
    print("kids is okay to ride.")