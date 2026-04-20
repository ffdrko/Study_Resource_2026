# Experiment - 1 use of boolean or operators
while True:
    user_action = input("Tpye add, show, edit, complete or exit: ")

    if "add" in user_action or 'new' in user_action:
        todo_item = user_action[4:] + "\n"

        with open("File/todo_list.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo_item)

        with open("File/todo_list.txt", "w") as file:
            file.writelines(todos)
    
    elif "show" in user_action:
        with open("File/todo_list.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")
    
    elif "edit" in user_action:
        number = int(user_action[5:])
        number = number - 1

        with open("File/todo_list.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter a new todo: ")
        todos[number] = new_todo + "\n"

        with open("File/todo_list.txt", "w") as file:
            file.writelines(todos)
    
    elif "complete" in user_action:
        number = int(user_action[9:])
        number = number - 1

        with open("File/todo_list.txt", "r") as file:
            todos = file.readlines()

        todos.pop(number)

        with open("File/todo_list.txt", "w") as file:
            file.writelines(todos)
    elif "exit" in user_action:
        break
    else:
        print("Command is not valid")