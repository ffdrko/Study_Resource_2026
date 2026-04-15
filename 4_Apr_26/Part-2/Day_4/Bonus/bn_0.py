filesnames = ["1.Raw Data.txt", "2.Cleaned Data.txt", "3.Analysis Results.txt"]
new_list = []

for file in filesnames:
    file = file.replace(" ", "_", 1)
    new_list.append(file)
    print(file)

print(filesnames)
print(new_list)