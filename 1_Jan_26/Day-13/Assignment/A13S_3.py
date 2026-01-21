def temp_checker(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"
    

print(temp_checker(10))
print(temp_checker(5))