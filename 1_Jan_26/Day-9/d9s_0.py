while True:
    user_action = input("Type 'add', 'show', 'edit', 'complete' or 'exit': ")

    match user_action:
        case 'add':
            todo_item = input("Enter a todo item: ")

            with open("1_Jan_26/Day-9/d9s_0.py", "r") as file:
                todo_list = file.readlines()


            todo_list.append(todo_item + "\n")

            with open("1_Jan_26/Day-9/d9s_0.py", "w") as file:
                file.writelines(todo_list)
        case 'show':
            with open("./file/todo_list.txt", "r") as file:
                todo_list = file.readlines()

            for index, item in enumerate(todo_list):
                item = item.strip("\n")
                print(f"{index + 1}-{item}")
        case 'edit':
            with open("./file/todo_list.txt", "r") as file:
                todo_list = file.readlines()

            todo_num = int(input("Enter the number of the todo item to edit: "))
            new_todo = input("Enter a new todo item: ")

            todo_list[todo_num - 1] = new_todo + "\n"

            with open("./file/todo_list.txt", "w") as file:
                file.writelines(todo_list)
        case 'complete':
            with open("./file/todo_list.txt", "r") as file:
                todo_list = file.readlines()

            todo_num = int(input("Enter the number of the todo item to complete: "))
            todo_list.pop(todo_num - 1)

            with open("./file/todo_list.txt", "w") as file:
                file.writelines(todo_list)
        case 'exit':
            break
new todo
