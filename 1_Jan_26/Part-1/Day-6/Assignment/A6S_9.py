filenames = ["a.txt", "b.txt", "c.txt"]

for filename in filenames:
    
    files = open(f"1_Jan_26/Day-6/File/{filename}", "r")
    content = files.read()
    print(content)