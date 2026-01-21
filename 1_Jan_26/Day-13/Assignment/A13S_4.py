def check_pass_lenght(password):
    if len(password) >= 8:
        return True
    else:
        return False
    

print(check_pass_lenght("mypassword12"))