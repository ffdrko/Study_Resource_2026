# Experiment - 2 return function

def greet():
    message = "Hello, World!" 
    new_message = message.capitalize()
    print("Hey")


greeting = greet()
print(greeting) # This will print None because the greet function does not have a return statement, so it returns None by default.