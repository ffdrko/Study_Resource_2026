try:
    width = float(input("Enter the width of the rectangle: "))
    length = float(input("Enter the length of the rectangle: "))

    if width == length:
        print("The rectangle is a square.")
        exit("Please enter different values for width and length to calculate the area of a rectangle.")
    else:
        area = width * length
        print(f"The area of the rectangle is: {area}")

   
except ValueError:
    print("Invalid input. Please enter numeric values for width and length.")