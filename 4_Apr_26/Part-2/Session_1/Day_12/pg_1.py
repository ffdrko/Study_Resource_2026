# when we declare a function, we define the paarameters that the function will take. When we call the function, we pass arguments to it. The parameters are like placeholders for the values that will be provided when the function is called.
def greet(message):
    new_message = message.capitalize()
    print("Hey Hey")
    return new_message

# when we call the function, we pass an argument to it. The argument is the actual value that we want to use in the function. In this case, we are passing the user_message variable as an argument to the greet function. The greet function will take this argument, process it, and return a new message that is capitalized. We then print the greeted_message to see the result.
user_message = input("Enter your message: ")
greeted_message = greet(user_message)
print(greeted_message)