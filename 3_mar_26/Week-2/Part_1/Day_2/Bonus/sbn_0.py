"""
Day-2 Bonus-1
Password checker
"""

password = input("Enter your password: ")

while password != "pass123":
    print("Wrong password")
    password = input("Enter your password: ")

print("welcome back user!!")