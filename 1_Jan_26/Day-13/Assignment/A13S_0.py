def get_age(brith_year, current_year = 2026):
    age = current_year - brith_year
    return age

user_birth_year = int(input("Enter your birth year: "))

user_Age = get_age(user_birth_year)
print(f"Your age is {user_Age} years.")