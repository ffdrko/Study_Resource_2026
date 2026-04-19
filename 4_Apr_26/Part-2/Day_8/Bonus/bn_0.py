user_date = input("Enter today's date: ")
user_mood = input("How do ypu rate your mood from 1 to 10? ")
user_content = input("Let your thoughts flow: ")

with open(f"File/{user_date}.txt", "w") as file:
    file.write(f"User mood rate {user_mood}")
    file.write(user_content)