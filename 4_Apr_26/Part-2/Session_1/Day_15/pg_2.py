# Your task is to create a program that 
# generates a random whole number. Here is how 
# the program should behave:

# As you can see, the program first asks the user 
# to enter a whole number. Then, once the user enters a number, 
# the program asks the user again to enter another number.

import random

num1 = int(input("Enter a whole number: "))
num2 = int(input("Enter another whole number: "))

random_num = random.randint(num1, num2)

print(f"The random whole number between {num1} and {num2} is: {random_num}")