def get_todos():
    with open("File/todo_list.txt", "r") as file:
        todo_list_local = file.readlines()
    return todo_list_local


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo_item = user_action[4:]

        todo_list = get_todos()

        todo_list.append(todo_item + "\n")

        with open("File/todo_list.txt", "w") as file:
            file.writelines(todo_list)
    
    elif user_action.startswith("show"):
        todo_list = get_todos()
        
        for index, item in enumerate(todo_list):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")
    
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            todo_list = get_todos()

            new_todo = input("Enter the new todo: ")
            todo_list[number - 1] = new_todo + "\n"

            with open("File/todo_list.txt", "w") as file:
                file.writelines(todo_list)
        except ValueError:
            print("Your command is not valid.")
            continue
    
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todo_list = get_todos()

            todo_list.pop(number - 1)

            with open("File/todo_list.txt", "w") as file:
                file.writelines(todo_list)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")