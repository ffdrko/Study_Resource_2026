"""
Problem 2: Dictionary Iteration & Unpacking

Given a dictionary of employee names and their monthly salaries:
salaries = {
    "Alvi": 52000,
    "Sadia": 68000,
    "Abir": 45000,
    "Tania": 72000,
    "Rifat": 49000
}

Tasks:
1. Iterate over the dictionary using `.items()` with tuple unpacking.
2. Print only the employees who earn 50,000 or more, in the format:
   "<Name> earns $<Salary> per month."
3. Print all employee names using `.keys()`.
"""

salaries = {
    "Alvi": 52000,
    "Sadia": 68000,
    "Abir": 45000,
    "Tania": 72000,
    "Rifat": 49000
}

# Write your code below:

for name, salary in salaries.items():
    if salary >= 50000:
        print(f"{name} earns ${salary} per month.")

for name in salaries.keys():
    print(name)