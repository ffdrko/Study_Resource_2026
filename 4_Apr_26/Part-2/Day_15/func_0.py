def get_todo(fiepath = "File/todo_list.txt"):
    """
        Reads the todo list from a file 
        and returns it as a list of strings.
    """
    with open(fiepath) as file:
        todo_list_local = file.readlines()
    return todo_list_local


def write_todo(todo_list_local, fiepath = "File/todo_list.txt"):
    """
        Writes the todo list to a file.
    """
    with open(fiepath, "w") as file:
        file.writelines(todo_list_local)

if __name__ == "__main__":
    print("These are the functions for the todo list application.")
    