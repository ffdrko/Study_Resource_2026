# Practice Problems: Number Guessing Game
# Solve each problem below. Run the file to check your output.

# 1. Number guessing game with 5 attempts
#    - Computer randomizes a number between 1-20
#    - User gets 5 attempts to guess
#    - After each guess, tell user "Too high" or "Too low"
#    - Print "You win!" if guessed correctly, "You lose!" if out of attempts


import random

computer = random.randint(1, 20)
count = 5

while count > 0:
    user_guess = int(input("Enter your guess: "))

    if user_guess == computer:
        print("Nice u do it")
        break
    elif computer > user_guess:
        print("Too low")
        count = count - 1
    elif computer < user_guess:
            print("Too high")
            count = count - 1

if count == 0:
     print("You lose")

# 2. Modify the game to give hints after each wrong guess
#    - Track the number of remaining attempts
#    - After each wrong guess, show how many attempts are left

import random

computer = random.randint(1, 20)
count = 5

while count > 0:
    user_guess = int(input("Enter your guess: "))

    if user_guess == computer:
        print("Nice u do it")
        break
    elif computer > user_guess:
        count = count - 1
        print(f"Too low, you have left {count}")
        
    elif computer < user_guess:
            count = count - 1
            print(f"Too high, you have left {count}")


if count == 0:
     print("You lose")