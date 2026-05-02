import time

user_name = input("Enter your name: ")
user_birth_year = int(input("Enter your birth year: "))

current_year = int(time.strftime("%Y"))

user_age = current_year - user_birth_year

print(f"The user age is {user_age} years of old")