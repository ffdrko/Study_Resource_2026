import random
computer = random.randint(1, 10)
# computer = 4

count = 3


while count > 0:
    guess = int(input("Enter your guess: "))

    count = count - 1

    if guess == computer:
        print("Nice u it's a match")

        break
    else:
        print("Wrong guess, Please Try again!")


print("End of trail")