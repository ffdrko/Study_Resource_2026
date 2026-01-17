try:
    user_total = float(input("Enter total number: "))
    user_num = float(input("Enter total number: "))

    percentage =  (user_num / user_total) * 100
    
    print(f"That is {percentage}")
except ValueError:
    print("You need to enter number, run the program again!")