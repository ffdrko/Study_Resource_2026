while True:
    user_action = input("Type 'add', 'show', 'edit', 'complete' or 'exit': ")

    match user_action:
        case 'add':
            todo_item = input("Enter a todo item: ")
            file = open("1_Jan_26/Day-8/file/todo_list.txt", "r")
            todo_list = file.readlines()
            file.close()

            todo_list.append(todo_item + "\n")

            file = open("1_Jan_26/Day-8/file/todo_list.txt", "w")
            file.writelines(todo_list)
            file.close()
        case 'show':
            file = open("1_Jan_26/Day-8/file/todo_list.txt", "r")
            todo_list = file.readlines()
            file.close()

            for index, item in enumerate(todo_list):
                item = item.strip("\n")
                print(f"{index + 1}-{item}")
        case 'edit':
            todo_num = int(input("Enter the number of the todo item to edit: "))
            new_todo = input("Enter a new todo item: ")

            todo_list[todo_num - 1] = new_todo + "\n"
        case 'complete':
            todo_num = int(input("Enter the number of the todo item to edit: "))
            todo_list.pop(todo_num - 1)
        case 'exit':
            break
