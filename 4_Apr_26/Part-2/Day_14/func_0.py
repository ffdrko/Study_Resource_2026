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

# This block will only execute if this script is run directly, and not when imported as a module.
if __name__ == "__main__":
    print("This is a module for handling todo items.")