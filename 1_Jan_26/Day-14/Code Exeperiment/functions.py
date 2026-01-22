def get_todo(filepath="Day-14/File/todo_list.txt"):
    """read the todo list from the file."""
    with open(filepath) as file:
        todo_local_list = file.readlines()
    return todo_local_list


def write_todo(todo_list_arg, filepath="Day-14/File/todo_list.txt"):
    """writing the todo item in the list"""
    with open(filepath, "w") as file:
        file.writelines(todo_list_arg)


if __name__ == "__main__":
    print("This is a module for todo list functions.")