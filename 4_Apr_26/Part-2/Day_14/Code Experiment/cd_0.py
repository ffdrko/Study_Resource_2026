# Experiment - 2 check the error of module file from the main file
# from func_0 import get_todo, write_todo
import cdfun_0 as func_0

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo_item = user_action[4:] + "\n"
        todo_list = func_0.get_todo()
        todo_list.append(todo_item)
        func_0.write_todo(todo_list)
    elif user_action.startswith("show"):
        todo_list = func_0. get_todo()
        for index, item in enumerate(todo_list):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            todo_list = func_0.get_todo()
            new_todo = input("Enter the new todo item: ") + "\n"
            todo_list[number - 1] = new_todo
            func_0.write_todo(todo_list)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todo_list = func_0.get_todo()
            todo_list.pop(number - 1)
            func_0.write_todo(todo_list)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Your command is not valid.")