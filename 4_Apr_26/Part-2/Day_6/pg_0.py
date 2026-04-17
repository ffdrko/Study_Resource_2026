while True:
    user_action = input("Enter add, show, edit, complete or exit: ")

    match user_action:
        case "add":
            file = open("File/todo_list.txt", "r")
            todo_list =file.readlines()

            todo_item = input("Enter a todo item: ") + "\n"
            todo_list.append(todo_item)
            file = open("File/todo_list.txt", "w")
            file.writelines(todo_list)
        case 'show':
            file = open("File/todo_list.txt", "r")
            todo_list =file.readlines()

            for index, item in enumerate(todo_list):
                print(f"{index + 1}. {item}")
        case 'edit':
            item_num = int(input("Enter the number of the item to edit: "))
            item_num -= 1
            todo_list[item_num] = input("Enter the new todo item: ")
        case 'complete':
            item_num = int(input("Enter the number of the item to edit: "))
            item_num -= 1
            todo_list.pop(item_num)
        case 'exit':
            break