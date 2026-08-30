# --- Dictionaries ---

students = {"Alvi": 23, "Sadia": 4, "Abir": 3}

## loop over keys
for student in students.items():
    print(student)

# --- Dictionaries ---


## loop over keys
for student in students.keys():
    print(student)


## loop over keys
for student in students.values():
    print(student)

## loop over keys
for student in students:
    print(student)

for student in students.items():
    name, roll = student
    print(name, roll)

for name, roll in students.items():
    print(name, roll )
