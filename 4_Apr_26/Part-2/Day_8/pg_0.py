while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    match user_action:
        case 'add':
            todo_item = input("Enter a todo item: ") + "\n"

            with open("File/todo_list.txt", "r") as file:
                todo_list = file.readlines()
            
            todo_list.append(todo_item)

            with open("File/todo_list.txt", "w") as file:
                file.writelines(todo_list)
        
        case 'show':
            with open("File/todo_list.txt", "r") as file:
                todo_list = file.readlines()

            for index, item in enumerate(todo_list):
                item = item.strip("\n")
                print(f"{index + 1}-{item}")
        
        case 'edit':
            with open("File/todo_list.txt", "r") as file:
                todo_list = file.readlines()

            item_num = int(input("Enter the number of todo item: "))
            item_num -= 1

            todo_list[item_num] = input("Enter the new todo: ") + "\n"

            with open("File/todo_list.txt", "w") as file:
                file.writelines(todo_list)
        
        case 'complete':
            with open("File/todo_list.txt", "r") as file:
                todo_list = file.readlines()
                
            item_num = int(input("Enter the number of todo item: "))
            item_num -= 1

            complete_todo = todo_list[item_num]

            todo_list.pop(item_num)

            with open("File/todo_list.txt", "w") as file:
                file.writelines(todo_list)
            
            print(f"{complete_todo.strip("\n")} is mark down and removed from the list.")
        
        case 'exit':
            break