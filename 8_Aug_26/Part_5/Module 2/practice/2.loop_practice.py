# Practice Problems: While Loops
# Solve each problem below. Run the file to check your output.

# 1. Print "Hello python" 10 times using a while loop

count = 0
while count < 10:
    print("Hello python")
    count = count + 1

print("-" * 30)

# 2. Print numbers 1 to 5 using a while loop

count = 1
while count <= 5:
    print(count)
    count = count + 1

print("-" * 30)

# 3. Count down from 10 to 1 using a while loop

count = 10
while count > 0:
    print(count)
    count = count - 1

print("-" * 30)

# 4. Ask the user to guess a number between 1-10 (use random.randint)
#    The user has 3 attempts to guess correctly

import random
computer = random.randint(1, 10)
count = 3

while count > 0:
    guess = int(input("Enter your guess: "))
    count = count - 1

    if guess == computer:
        print("Nice! It's a match")
        break
    else:
        print("Wrong guess, Please Try again!")

print("End of trail")