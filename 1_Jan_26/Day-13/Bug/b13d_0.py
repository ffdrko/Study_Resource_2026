def calculate(h, g = 9.8):
    t = (2 * h / g) ** 0.5
    return t

cal = calculate(100)
print(cal)