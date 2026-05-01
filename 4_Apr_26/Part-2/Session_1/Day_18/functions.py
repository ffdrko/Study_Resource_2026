FILEPATH = "File/todo_list.txt"

def get_todo():
    """
    Reads the todo list from the file and 
    returns it as a list of strings.
    """
    with open(FILEPATH, 'r') as file:
        todos = file.readlines()
    return todos


def write_todo(todos):
    """
    Writes the given list of todos to the file.
    Each todo is written on a new line.
    """
    with open(FILEPATH, 'w') as file:
        file.writelines(todos)

if __name__ == "__main__":
    print("This module provides functions to read and write a todo list from a file.")