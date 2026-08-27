# Practice Problems: Number Guessing Game
# Solve each problem below. Run the file to check your output.

# 1. Number guessing game with 5 attempts
#    - Computer randomizes a number between 1-20
#    - User gets 5 attempts to guess
#    - After each guess, tell user "Too high" or "Too low"
#    - Print "You win!" if guessed correctly, "You lose!" if out of attempts

import random
computer = random.randint(1, 20)
attempts = 5

print("I'm thinking of a number between 1 and 20!")

for attempt in range(attempts):
    guess = int(input(f"Attempt {attempt + 1}: Enter your guess: "))

    if guess == computer:
        print("You win!")
        break
    elif guess < computer:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"You lose! The number was {computer}")

# 2. Modify the game to give hints after each wrong guess
#    - Track the number of remaining attempts
#    - After each wrong guess, show how many attempts are left

import random
computer = random.randint(1, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Enter your guess: "))
    attempts = attempts - 1

    if guess == computer:
        print("Nice! It's a match!")
        break
    elif guess < computer:
        print(f"Too low! {attempts} attempts remaining.")
    else:
        print(f"Too high! {attempts} attempts remaining.")

if attempts == 0:
    print(f"Game over! The number was {computer}")