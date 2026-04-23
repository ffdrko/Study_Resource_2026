filenames = ["1. doc", "2. report", "3. presentation"]

file = [item.replace(". ", "-") + ".txt" for item in filenames]

print(file)