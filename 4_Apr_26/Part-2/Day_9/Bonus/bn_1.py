password = input("Enter the password: ")

result = dict()
pass_length = False

if len(password) >= 8:
    pass_length = True

result["pass_length"] = pass_length

pass_upper = False


for char in password:
    if char.isupper():
        pass_upper = True

result["pass_upper"] = pass_upper

pass_digit = False

for num in password:
     if num.isdigit():
        pass_digit = True

result["pass_digit"] = pass_digit

if all(result.values()):
    print("Password is strong.")
else:
    print("Password is not strong.")

print(result)