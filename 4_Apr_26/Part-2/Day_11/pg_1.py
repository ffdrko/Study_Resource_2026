def greet():
    message = "Hello, World!" 
    new_message = message.capitalize()
    return new_message


greeting = greet()
print(greeting)

# print(new_message) will not work because new_message is a local variable inside the greet function and cannot be accessed outside of it.