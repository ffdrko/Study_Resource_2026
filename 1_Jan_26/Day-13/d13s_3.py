# use default parameters for the path
def get_todo(filepath = '1_Jan_26/Day-13/Files/todo_list.txt'):
    """Read the todo list from a file and return it as a list of strings"""

    with open(filepath) as file:
        todo_local_list = file.readlines()
    return todo_local_list


def write_todo(todo_list_arg, filepath = '1_Jan_26/Day-13/Files/todo_list.txt'):
    """Write the todo list to a file from a list of strings"""

    with open(filepath, 'w') as file:
        file.writelines(todo_list_arg)


print(help(get_todo))
while True:
    user_action = input("Type add, show, edit, complete and exit: ")

    if user_action.startswith('add'):
        todo_item = user_action[4:] + '\n'
        todo_list = get_todo()

        todo_list.append(todo_item)

        write_todo(todo_list)
    
    elif user_action.startswith('show'):
        todo_list = get_todo()

        for index, item in enumerate(todo_list):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")
    
    elif user_action.startswith('edit'):
        try:
            todo_num = int(user_action[5:]) - 1
            todo_list = get_todo()

            todo_list[todo_num] = input("Enter a new edited todo item: ") + '\n'

            write_todo(todo_list)

        except ValueError:
            print("Enter number after edit.")
    
    elif user_action.startswith('complete'):
        try:
            todo_num = int(user_action[9:]) - 1
            todo_list = get_todo()

            todo_list.pop(todo_num)

            write_todo(todo_list)

        except IndexError:
            print("The number you entered is out of the list range.")
    
    elif user_action.startswith('exit'):
        break

    else:
        print("Command not valid.") 