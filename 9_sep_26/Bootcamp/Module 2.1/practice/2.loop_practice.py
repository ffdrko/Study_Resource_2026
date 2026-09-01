# Practice Problems: While Loops
# Solve each problem below. Run the file to check your output.

# 1. Print "Hello python" 10 times using a while loop
count = 1

while count <= 10:
    print("Hello python")
    count = count + 1

# 2. Print numbers 1 to 5 using a while loop
count = 1
while count <= 5:
    print(count)
    count = count + 1
# 3. Count down from 10 to 1 using a while loop
count = 10
while count >= 1:
    print(count)
    count = count - 1
# 4. Ask the user to guess a number between 1-10 (use random.randint)
#    The user has 3 attempts to guess correctly

import random

count = 3 
computer = random.randint(1, 10)

while count > 0:
    user_guess = int(input("Enter your guess: "))

    if user_guess == computer:
        print("Nice u do it")
        break
    else:
        count = count - 1
        print(f"Wrong ansewer, you have {count} guess left")