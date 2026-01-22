def temp_checker(temp):
    if temp > 25:
        return 'HOT'
    elif 15 <= temp <= 25:
        return 'Warm'
    else:
        return 'cool'
    
print(temp_checker(18))