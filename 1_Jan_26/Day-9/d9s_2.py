while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo_item = user_action[4: ]

        with open("1_Jan_26/Day-9/file/todo_list.txt") as file:
            todo_list = file.readlines()

        todo_list.append(todo_item + "\n")

        with open("1_Jan_26/Day-9/file/todo_list.txt", "w") as file:
            file.writelines(todo_list)
    
    elif 'show' in user_action:
        with open("1_Jan_26/Day-9/file/todo_list.txt") as file:
            todo_list = file.readlines()

        for index, item in enumerate(todo_list):
            item = item.strip("\n")
            print(f"{index + 1}-{item}")
    elif 'edit' in user_action:
        todo_num = int(user_action[5:]) - 1

        with open("1_Jan_26/Day-9/file/todo_list.txt") as file:
            todo_list = file.readlines()    
        
        todo_list[todo_num] = input("Enter a new todo: ") + "\n"

        with open("1_Jan_26/Day-9/file/todo_list.txt", "w") as file:
            file.writelines(todo_list)
    elif 'complete' in user_action:
        
        todo_num = int(input("Enter the number of todo to complete: ")) - 1

        with open("1_Jan_26/Day-9/file/todo_list.txt") as file:
            todo_list = file.readlines()    
        
        todo_list.pop(todo_num)

        with open("1_Jan_26/Day-9/file/todo_list.txt", "w") as file:
            file.writelines(todo_list)
    elif 'exit' in user_action:
        break         