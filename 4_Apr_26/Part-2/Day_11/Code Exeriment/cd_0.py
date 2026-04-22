# Experiment - 1 function definition and function call

# This part is function definition. We are defining a function named greet that takes no parameters and returns a string.
def greet():
    message = "Hello, World!" 
    new_message = message.capitalize()
    print("Hey")
    return new_message

# This part is function call. We are calling the greet function and storing its return value in the variable greeting, then printing it.
greeting = greet()
print(greeting)