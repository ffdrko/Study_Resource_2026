while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    match user_action:
        case "add":
            todo_item = input("Enter a todo item:") + "\n"

            file = open("1_Jan_26/Day-7/File/todo_list.txt", "r")
            todo_list = file.readlines()

            todo_list.append(todo_item)

            file = open("1_Jan_26/Day-7/File/todo_list.txt", "w")
            file.writelines(todo_list)
        
        case "show":
            file = open("1_Jan_26/Day-7/File/todo_list.txt", "r")
            todo_list = file.readlines()
            file.close()

            new_todo_list = []

            for item in todo_list:
                new_item = item.strip("\n")
                new_todo_list.append(new_item)

            for index, item in enumerate(new_todo_list):
                print(f"{index + 1}-{item}")
        case "edit":
            item_number = int(input("Enter the number of the item to edit: "))
            new_todo = input("Enter the new todo item: ") + "\n"

            todo_list[item_number - 1] = new_todo
        case "complete":
            item_number = int(input("Enter the number of the item to edit: "))

            todo_list.pop(item_number - 1)
        case "exit":
            break