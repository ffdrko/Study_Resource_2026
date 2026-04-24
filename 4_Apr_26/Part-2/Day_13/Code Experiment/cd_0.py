# Experiment -1 use of doc string

def get_todo(file_path = "File/todo_list.txt"):
    """Read a text file and return the list of to-dos."""
    with open(file_path) as file:
        todo_list_local = file.readlines()
    return todo_list_local


def write_todo(todo_list_local, file_path = "File/todo_list.txt"):
    """Write a list of to-dos to a text file."""
    with open(file_path, "w") as file:
        file.writelines(todo_list_local)


text = """
------Welconme to the To-Do List App------
Choose one of the following commands:
add <todo> - Add a new to-do item
show - Display all to-do items
edit <number> - Edit a specific to-do item
complete <number> - Mark a to-do item as complete
exit - Exit the application

"""
print(text)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    

    if user_action.startswith("add"):
        user_todo = user_action[4:] + "\n"

        todo_list = get_todo()

        todo_list.append(user_todo)

        write_todo(todo_list)

    elif user_action.startswith("show"):
        todo_list = get_todo()

        for index, item in enumerate(todo_list):
            item = item.strip("\n")   
            print(f"{index + 1}-{item}")
    
    elif user_action.startswith("edit"):
        try:
            todo_list = get_todo()

            user_todo_num = int(user_action[5:]) - 1
            
            todo_list[user_todo_num] = input("Enter new todo: ") + "\n"

            write_todo(todo_list)
        except ValueError:
            print("Enter number after the command.")
    
    elif user_action.startswith("complete"):
        try:
            todo_list = get_todo()

            user_todo_num = int(user_action[9:])
            
            todo_list.pop(user_todo_num - 1)

            write_todo(todo_list)
        except IndexError:
            print("The number you enter is not in the list.")
    
    elif user_action.startswith("exit"):
        break
    
    else:
        print("Wrong command")
