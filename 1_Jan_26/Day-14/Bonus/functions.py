def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    return feet, inches

def convert(feet, inche):
    meters = feet * 0.3048 +inche * 0.0254
    return meters