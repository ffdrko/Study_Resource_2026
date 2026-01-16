user_date = input("Enter Today's date: ")
user_mood = input("How do you rate your mood today from 1 to 10: ")
user_thougths = input("Let your thoughts flow: ")

with open(f"1_Jan_26/Day-8/Journal/{user_date}.txt", "w") as file:
    file.write(user_mood + "\n")
    file.write(user_thougths)