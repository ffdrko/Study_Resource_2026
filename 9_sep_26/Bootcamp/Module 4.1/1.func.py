def greet(name = "Guest"):
    print(f"hello, {name}")
    print(f"how are you {name}?")

greet()
greet("Deepto")


def normalize(value, maxvalue):
    normalize_Value = value/ maxvalue
    print(f"the normalize value is {normalize_Value}")


normalize(50000, 100000)