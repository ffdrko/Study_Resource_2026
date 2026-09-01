# import random

# cards = ["king", "queen", "Jack"]

# choice = random.choice(cards)

# print(choice)


# ## Number guessing game

# computer = random.randint(1, 5)

# while True:
#     guess = int(input("Try to guess the number: "))

#     if guess == computer:
#         print("hurray")
#         break

## datetime

from datetime import datetime, date

today = datetime.today()

print(today.strftime("Date: %Y-%m-%d  Time: %H:%M:%S  Day: %A"))