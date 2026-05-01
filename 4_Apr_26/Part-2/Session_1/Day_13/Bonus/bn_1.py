feet_inches = input("Enter the number of feet: ")

def parse(feet_inches):
    parts = feet_inches.split()
    feet = float(parts[0]) 
    inches = float(parts[1])
    return feet, inches


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


feet, inches  = parse(feet_inches)
result = convert(feet, inches)

print(result)
if result < 1:
    print("Kid is too short to ride the roller coaster.")
else:    
    print("Kid is tall enough to ride the roller coaster.")