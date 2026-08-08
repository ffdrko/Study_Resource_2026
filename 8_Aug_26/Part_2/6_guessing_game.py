import random

computer_choice = random.choice(['Jack', 'Queen', 'King'])

while True:
    user_choice = input("Enter your choice (Jack, Queen, King): ").title()
    if user_choice == computer_choice:
        print("You guessed it right! The computer chose:", computer_choice)
        break
    else:
        print("Wrong guess! Try again.")