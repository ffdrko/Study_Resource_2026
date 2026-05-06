import time

with open("File/content.txt") as file:
    content = file.read()

time_info = time.strftime("%d %b %Y")

with open("File/new_content.txt", "w") as file:
    file.write(f"Date:{time_info}" + "\n")
    file.write(content)

print("new_Content available.")