def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return maximum


cels = get_maximum()
fahrenheit = cels * 1.8 + 3.2

print(fahrenheit)