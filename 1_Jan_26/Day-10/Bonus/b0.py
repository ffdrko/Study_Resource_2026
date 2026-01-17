try:
    width = float(input("Enter width: "))
    length = float(input("Enter length: "))

    if width == length:
        exit("width and length are equal, it will be a square.")

    area = width * length
    print(area)
except ValueError:
    print("please enter a number")