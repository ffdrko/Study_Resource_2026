# Practice Problems: Conditional Statements
# Solve each problem below. Run the file to check your output.

# 1. Given age = 20, use if/elif/else to print:
#    - "You are adult" if age >= 18
#    - "You are teen" if age < 18 and age >= 13
#    - "You are child" if age < 13

age = 20

if age >= 18:
    print("You are adult")
elif age <18 and age >= 13:
    print("You are teen")
else:
    print("You are child")

# 2. Given score = 85, use if/elif/else to print:
#    - "Grade A" if score >= 90
#    - "Grade B" if score >= 80 and score < 90
#    - "Grade C" if score >= 70 and score < 80
#    - "Grade D" otherwise

score = 85

if score >= 90:
    print("Grade is A")
elif score >= 80 and score < 90:
    print("Grade is B")
elif score >= 70 and score < 80:
    print("Grade C")
else:
    print("Grade is D")

# 3. Write a program that asks the user for their age and prints:
#    - "You are eligible for driving" if age >= 18
#    - "You are teen" if age >= 13 and age < 18
#    - "You are child" if age < 13

user_input = int(input("Enter your age: "))

if user_input >= 18:
    print("You are eligible for driving")
elif user_input >= 13 and user_input < 18:
    print("You are teen")
else:
    print("You are child")