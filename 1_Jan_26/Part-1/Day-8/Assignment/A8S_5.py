with open("1_Jan_26/Day-8/file/story.txt") as file:
    content = file.read()

with open("1_Jan_26/Day-8/file/story.txt", "w") as file:
    file.write(content)