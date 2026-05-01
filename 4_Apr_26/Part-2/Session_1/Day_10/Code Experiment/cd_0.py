# Experiment - 1 Types of errors
# 1. Syntax error - when the code is not written in the correct format. For example, missing a parenthesis or a colon.
# 2. Logical error - when the code runs but produces incorrect results.
# 3. Runtime error - when the code fails during execution.

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        with open("File/todo_list.txt", "r") as file:
            todo_list = file.readlines()

        todo_list.append(todo + "\n")

        with open("File/todo_list.txt", "w") as file:
            file.writelines(todo_list)
    
    elif user_action.startswith("show"):
        with open("File/todo_list.txt", "r") as file:
            todo_list = file.readlines()

        for index, item in enumerate(todo_list):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")
    
    elif user_action.startswith("edit"):
        try:
            todo_number = int(user_action[5:])
            todo_number -= 1

            with open("File/todo_list.txt", "r") as file:
                todo_list = file.readlines()

            new_todo = input("Enter the new todo: ")
            todo_list[todo_number] = new_todo + "\n"

            with open("File/todo_list.txt", "w") as file:
                file.writelines(todo_list)
        except ValueError:
            print("After edit, please enter a valid number.")
            continue
    elif user_action.startswith("complete"):
        try:
            todo_number = int(user_action[9:])
            todo_number -= 1

            with open("File/todo_list.txt", "r") as file:
                todo_list = file.readlines()

            todo_list.pop(todo_number)

            with open("File/todo_list.txt", "w") as file:
                file.writelines(todo_list)
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")