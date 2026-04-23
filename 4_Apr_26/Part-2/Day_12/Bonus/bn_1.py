def convert(feet_icnhes):
    path = feet_icnhes.split(" ")
    
    feet = float(path[0])
    inches = float(path[1])

    meters = feet * 0.3048 + inches * 0.0254
    
    return meters

feet_inches = input("Enter feet and inches: ")

print(convert(feet_inches))

if convert(feet_inches) < 1:
    print("kid is too small")
else:
    print("kid is big enough")