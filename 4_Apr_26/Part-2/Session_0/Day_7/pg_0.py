while True:
    user_action = input("Enter add, show, edit, complete or exit: ")

    match user_action:
        case "add":
            file = open("File/todos.txt", "r")
            todo_list = file.readlines()
            file.close()

            todo_item = input("Enter a todo item: ") + "\n"
            todo_list.append(todo_item)

            file = open("File/todos.txt", "w")
            file.writelines(todo_list)
            file.close()
        case "show":
            file = open("File/todos.txt", "r")
            todo_list = file.readlines()
            file.close()

            for index, item, in enumerate(todo_list):
                item = item.strip("\n")
                print(f"{index + 1}. {item}")
        case "edit":
            item_no = int(input("Enter the number of the item you want to edit: "))
            item_no -= 1
            todo_list[item_no] = input("Enter the new todo item: ") + "\n"

        case "complete":
            item_no = int(input("Enter the number of the item you want to edit: "))
            item_no -= 1
            todo_list.pop(item_no)
        case "exit":
            break