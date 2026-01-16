languages = ['English', 'Bangla', 'Hindi']

for item in languages:
    with open(f"1_Jan_26/Day-8/file/{item}.txt", "w") as file:
        file.write(item)