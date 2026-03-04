"""
Day-2 Bonus
Password checker
"""

password = input("Enter your password: ")

while password != "pass123":
    print("Wrong password")
    password = input("Enter your password: ")

print("welcome back user!!")