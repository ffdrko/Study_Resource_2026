user_password = input("Enter your password: ")

while user_password != "pass123":
    print("Incorrect password. Please try again.")
    user_password = input("Enter your password: ")

print("Access granted. Welcome!")