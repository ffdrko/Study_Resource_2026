filenames = ["1.Raw data.txt", "2.Processed data.txt", "3.Summary report.txt"]

for filename in filenames:
    filename = filename.replace(".", "-", 1)
    print(filename)