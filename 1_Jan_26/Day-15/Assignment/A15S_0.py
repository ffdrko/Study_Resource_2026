import random

user_lower_num = int(input("Enter the lower bound: "))
user_upper_num = int(input("Enter the upper bound: "))

print(f"Your random number is: {random.randint(user_lower_num, user_upper_num)}")