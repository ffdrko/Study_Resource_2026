todo_list = []

while True:
    user_action = input("Type 'add', 'show', 'edit' or 'exit': ")
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            todo_item = input("Enter a to-do item: ")
            todo_list.append(todo_item)
        case 'show':
            for item in todo_list:
                print(item)
        case 'edit':
            item_number = int(input("Enter the number of the item to edit: ")) - 1
            todo_list[item_number] = input("Enter the new to-do item: ")
        case 'exit':
            break

print("Goodbye!")