def get_todo(file_path):
    with open(file_path) as file:
        todo_list_local = file.readlines()
    return todo_list_local

def write_todo(file_path, todo_list_local):
    with open(file_path, "w") as file:
        file.writelines(todo_list_local)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    if user_action.startswith("add"):
        todo_item = user_action[4:]
        user_action = user_action.strip()

        todo_list = get_todo("File/todo_items.txt")
        todo_list.append(todo_item + "\n")

        write_todo("File/todo_items.txt", todo_list)
    
    elif user_action.startswith("show"):
        todo_list = get_todo("File/todo_items.txt")
        for index, item in enumerate(todo_list):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")
    
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todo_list = get_todo("File/todo_items.txt")
            new_todo = input("Enter the new todo item: ")
            todo_list[number] = new_todo + "\n"

            write_todo("File/todo_items.txt", todo_list)

        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number - 1

            todo_list = get_todo("File/todo_items.txt")
            todo_list.pop(number)

            write_todo("File/todo_items.txt", todo_list)
            
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("exit"):
        break
    else:        
        print("Command is not valid.")