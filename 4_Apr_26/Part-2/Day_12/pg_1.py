def greet(message):
    new_message = message.capitalize()
    print("Hey Hey")
    return new_message


user_message = input("Enter your message: ")
greeted_message = greet(user_message)
print(greeted_message)