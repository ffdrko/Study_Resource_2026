todo_list = []

while True:
    user_action = input("Enter add, show oor exit: ")

    match user_action:
        case "add":
            user_todo = input("Enter a todo: ")
            todo_list.append(user_todo)
        case "show":
            print(todo_list)