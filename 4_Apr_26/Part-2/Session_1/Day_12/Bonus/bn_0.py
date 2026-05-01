def convert(feet_icnhes):
    path = feet_icnhes.split(" ")
    
    feet = float(path[0])
    inches = float(path[1])

    meters = feet * 0.3048 + inches * 0.0254
    
    return f"{feet} feet and {inches} inches is equal to {meters:.2f} meters."

feet_inches = input("Enter feet and inches: ")

print(convert(feet_inches))