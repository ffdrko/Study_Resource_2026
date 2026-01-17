# Bug-Fixing Exercise 1
# Have a look at the program below:

# waiting_list = ["john", "marry"]
# name = input("Enter name: ")

# number = waiting_list.index(name)
# print(f"{name}'s turn is {number}")
   

try:
    waiting_list = ["john", "marry"]
    name = input("Enter name: ")

    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")   
except ValueError:
    print(f"{name} is not register in the list.")