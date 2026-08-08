text = "Hello world!"

print(text.upper())
print(text.lower())
print(text.strip().title())

print(text.count("o"))

print(text.replace("world", "Bangladesh"))
print(len(text))
print(text.startswith("Hello"))
print(text.endswith("python"))

sentence = "I am learning Python programming."

print(sentence.split())
print(sentence.split("Python"))
print(sentence.split("Python", 1))
print(sentence.split("learning", 2))
print(sentence.find("gram"))
print(text.index("o"))
print(text.find("o"))

num = "123n"

print(num.isdigit())
print(num.isnumeric())
print(num.isalnum())
