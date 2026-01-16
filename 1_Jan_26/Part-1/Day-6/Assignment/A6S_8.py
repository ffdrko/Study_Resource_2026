filenames = ["d.txt", "r.txt", "g.txt"]

for file in filenames:

    file = open(f"1_Jan_26/Day-6/File/{file}", "w")
    file.writelines("Hello")