filesnames = ["1.Raw Data.txt", "2.Cleaned Data.txt", "3.Analysis Results.txt"]

for file in filesnames:
    print(file.replace(".", "_", count=1))