# from google.colab import drive
# drive.mount('/content/drive')

file = open("File/sample.txt", "w")
file.write("Hello World\n")
file.write("Ostad\n")
file.write("Mastering the python\n")
file.close()

file = open("File/sample.txt", "r")
content = file.readlines()
print(content)
file.close()

file = open("File/sample.txt", "a")
file.write("new line added by append\n")
file.close()