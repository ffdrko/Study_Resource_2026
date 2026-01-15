# using read second time will not give any output
with open("1_Jan_26/Day-8/file/doc.txt", "r") as file:
    file.read()
    content = file.read()

print(content)