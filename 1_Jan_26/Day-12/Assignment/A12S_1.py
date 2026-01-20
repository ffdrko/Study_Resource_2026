def check_password(password):
    result = {}
    if len(password) >= 8:
        result['length'] = True
    else:
        result['length'] = False
    
    result['uppercase'] = False
    result['isnumber'] = False

    for i in password:
        if i.isupper():
            result['uppercase'] = True
        if i.isdigit():
            result['isnumber'] = True
    
    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"

pass_check = check_password("Pass12Word")    

print(pass_check)