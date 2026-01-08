todo_list = []

while True:
    user_action = input("Type add, show, or exit: ")

    match user_action:
        case "add":
            todo_item = input("Enter a todo: ")
            todo_list.append(todo_item)
        case "show":
            print(todo_list)
        case "exit":
            break

print("Goodbye!")