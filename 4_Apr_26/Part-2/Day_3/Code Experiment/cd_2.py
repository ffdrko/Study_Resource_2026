# Experiment - 3  For-loop

todo_list = []

while True:
    user_action = input("Enter add, show oor exit: ")

    match user_action:
        case "add":
            user_todo = input("Enter a todo: ")
            todo_list.append(user_todo)
        case "show"| "Display":
            for i in todo_list:
                i = i.title()
                print(i)
        case "exit":
            break
        case _:
            print("Please enter a valid command")

print("Bye!")