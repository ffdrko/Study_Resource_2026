todo_list = []

while True:
    user_action = input("Type add, show, edit, complete or exit:")

    match user_action:
        case "add":
            todo_item = input("Enter a todo item: ")
            todo_list.append(todo_item)
        
        case "show":
            for index, item in enumerate(todo_list):
                print(f"{index + 1}-{item}")
        case "edit":
            item_number = int(input("Enter the number of the item to edit: "))
            item_number = item_number - 1
            todo_list[item_number] = input("Enter the new todo item: ")
        case "complete":
            item_number = int(input("Enter the number of the item is complete: "))
            item_number = item_number - 1
            todo_list.pop(item_number)
        case "exit":
            break