todo_list = []

while True:
    user_action = input("Type 'add', 'show', 'edit', 'complete' or 'exit': ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todo_list.append(todo)
        case 'show':
            for index, item in enumerate(todo_list):
                row = f"{index}-{item}"
                print(row)
        case 'edit':
            number = int(input("Enter the number of the todo to edit: "))
            new_todo = input("Enter the new todo: ")
            todo_list[number - 1] = new_todo
        case 'complete':
            item_number = int(input("Enter the number of todoo item: "))
            item_number = item_number - 1
            todo_list.pop(item_number)
        case 'exit':
            break