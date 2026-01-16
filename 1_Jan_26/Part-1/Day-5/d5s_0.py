todo_list = []

while True:
    user_action = input("Type 'add', 'show', 'edit', or 'exit': ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todo_list.append(todo)
        case 'show':
            for item in todo_list:
                print(item)
        case 'edit':
            number = int(input("Enter the number of the todo to edit: "))
            new_todo = input("Enter the new todo: ")
            todo_list[number - 1] = new_todo
        case 'exit':
            break