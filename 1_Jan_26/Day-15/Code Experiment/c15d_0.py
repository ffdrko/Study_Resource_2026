import glob

myfiles = glob.glob("../file/*.txt")


for path in myfiles:
    with open(path) as f:
        file_Content = f.readlines()
    print(file_Content)

print(myfiles)