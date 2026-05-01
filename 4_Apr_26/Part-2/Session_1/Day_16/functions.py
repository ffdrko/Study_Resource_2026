FILEPATH = "File/todo_list.txt"
def get_todo():
    """
    Reads the todo list from the file and 
    returns it as a list of strings.
    """
    
    with open(FILEPATH, "r") as file:
        todo_list_local = file.readlines()
    return todo_list_local


def write_todo(todo_list_local):
    """
    writes the given list of strings to the file,
    overwriting the existing content.
    """
    with open(FILEPATH, "w") as file:
        file.writelines(todo_list_local)