password = input("Enter your passowrd: ")

score = []

if len(password) >= 8:
    score.append(True)
else:
    score.append(False)

digit = False
for index in password:
    if index.isdigit():
        digit = True

score.append(digit)

upper = False
for index in password:
    if index.isupper():
        upper = True

score.append(upper)

if all(score):
    print("stronge password")
else:
    print("WEAK PASSWORD!")