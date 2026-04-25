def get_todo(file_path = "File/todo_item.txt"):
    """
    Retrieve the list of todo items from a file.
    
    """
    with open(file_path) as file:
        todo_list_local = file.readlines()
    return todo_list_local


def write_todo(todo_list_local, file_path = "File/todo_item.txt"):
    """
    Write the list of todo items to a file.
    
    """
    with open(file_path, "w") as file:
        file.writelines(todo_list_local)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo_item = user_action[4:] + "\n"
        todo_list = get_todo()
        todo_list.append(todo_item)
        write_todo(todo_list)
    elif user_action.startswith("show"):
        todo_list = get_todo()
        for index, item in enumerate(todo_list):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            todo_list = get_todo()
            new_todo = input("Enter the new todo item: ") + "\n"
            todo_list[number - 1] = new_todo
            write_todo(todo_list)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todo_list = get_todo()
            todo_list.pop(number - 1)
            write_todo(todo_list)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Your command is not valid.")