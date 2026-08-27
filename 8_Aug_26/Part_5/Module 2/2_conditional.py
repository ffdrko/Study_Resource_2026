age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligble for driving")
else:
    print("You are eligle for not driving")


if age < 13:
    print("You are child")
elif age < 18:
    print("You are teen")
else:
    print("you are adult")