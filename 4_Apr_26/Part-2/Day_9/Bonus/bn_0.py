password = input("Enter the password: ")

result = []
pass_length = False

if len(password) >= 8:
    pass_length = True

result.append(pass_length)

pass_upper = False


for char in password:
    if char.isupper():
        pass_upper = True

result.append(pass_upper)

pass_digit = False

for num in password:
     if num.isdigit():
        pass_digit = True

result.append(pass_digit)

if all(result):
    print("Password is strong.")
else:
    print("Password is not strong.")