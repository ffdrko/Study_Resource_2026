# Check grade based on the mark entered by the user

# Taking the mark from the user
mark = int(input("Enter your mark (0-100): "))

# Checking the mark is valid
if mark < 0 or mark > 100:
    print("Invalid mark! Please enter a value between 0 and 100.")
else:
    # Determining the grade using if-elif-else
    if mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 50:
        grade = "D"
    else:
        grade = "F"

    print(f"Your mark is {mark}. Your grade is {grade}.")
