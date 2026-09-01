# Practice Problems: input(), Concatenation & Formatting
# Solve each problem below.

# 1. Ask the user for their name and print: Hello, <name>!

user_name = input("Enter your name: ")

print(f"Hello, {user_name}")

# 2. Ask for two numbers and print their sum.
#    Hint: input() gives strings — you need type conversion!

first_num = float(input("Enter the first number: "))
second_num = float(input("Enter the second number: "))

result = first_num + second_num

# print(f"The total sum of number is {result}")
# 3. Ask for the user's birth year and calculate their age (assume current year is 2026).
#    Print: You are about <age> years old

user_birthday = input("Enter your bath year: ")
current_year = 2026

user_age = 2026 - int(user_birthday)

print(f"You are about {user_age} years old")
# 4. Using f-strings, given name = "Deepto" and score = 95,
#    print: Deepto scored 95 marks!
given_name = "Deepto"
score = 95

print(f"{given_name} scored {score} marks!")

# 5. Ask the user for a word and a number n.
#    Print the word repeated n times using string multiplication.

user_word = input("Enter a word: ")
repeated_num = int(input("Enter repeated number: "))

print(user_word * repeated_num)
