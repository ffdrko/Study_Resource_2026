try:
    user_total_num = float(input("Enter total number: "))
    user_num = float(input("Enter value: "))

    divison = user_num / user_total_num
    print(divison)
except ZeroDivisionError:
    print("Your value cannot be zero")