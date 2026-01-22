def get_todo(filepath="Day-14/File/todo_list.txt"):
    """read the todo list from the file."""
    with open(filepath) as file:
        todo_local_list = file.readlines()
    return todo_local_list


def write_todo(todo_list_arg, filepath="Day-14/File/todo_list.txt"):
    """writing the todo item in the list"""
    with open(filepath, "w") as file:
        file.writelines(todo_list_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    if user_action.startswith("add"):
        todo_item = user_action[4:] + "\n"
        todo_list = get_todo()
        todo_list.append(todo_item)
        write_todo(todo_list)
    
    elif user_action.startswith("show"):
        todo_list = get_todo()

        for index, item in enumerate(todo_list):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")

    elif user_action.startswith("edit"):
        item_num = int(user_action[5:])
        todo_list = get_todo()

        todo_list[item_num - 1] = input("Enter new todo item: ") + '\n'

        write_todo(todo_list)

    elif user_action.startswith('complete'):
        item_num = int(user_action[9:]) - 1
        todo_list = get_todo()

        todo_list.pop(item_num)

        write_todo(todo_list)

    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid comment!!")