filesnames = ("1.Raw Data.txt", "2.Cleaned Data.txt", "3.Analysis Results.txt")

for file in filesnames:
    file = file.replace(" ", "_", 1)
    print(file)

print(filesnames)