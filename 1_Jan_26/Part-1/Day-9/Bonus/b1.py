password = input("Enter your passowrd: ")

score = dict()

if len(password) >= 8:
    score["length"] = True
else:
    score['length'] = False

digit = False
for index in password:
    if index.isdigit():
        digit = True

score['digits'] = digit

upper = False
for index in password:
    if index.isupper():
        upper = True

score["uppercase"] = upper

print(score)

if all(score.values()):
    print("stronge password")
else:
    print("WEAK PASSWORD!")