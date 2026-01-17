FILE_PATH = "./Files/todo_list.txt"

while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    if user_action.startswith('add'):
        todo_item = user_action[4:] + '\n'

        with open(FILE_PATH) as file:
            todo_list = file.readlines()

        todo_list.append(todo_item)

        with open(FILE_PATH, 'w') as file:
            file.writelines(todo_list)

    elif user_action.startswith('show'):
        with open(FILE_PATH) as file:
            todo_list = file.readlines()

        for index, item in enumerate(todo_list):
            item = item.strip("\n")
            print(f"{index+1}-{item}")
    elif user_action.startswith('edit'):
        try:
            todo_item = int(user_action[5:])
            with open(FILE_PATH) as file:
                todo_list = file.readlines()

            todo_list[todo_item-1] = input("Enter new item to add: ") + '\n'

            with open(FILE_PATH, 'w') as file:
                file.writelines(todo_list)
        except ValueError:
            print("use item number after edit.")
    elif user_action.startswith('complete'):
        try:
            todo_num = int(user_action[9:]) - 1

            with open(FILE_PATH) as file:
                todo_list = file.readlines()

            todo_list.pop(todo_num)

            with open(FILE_PATH, "w") as file:
                file.writelines(todo_list)
        except IndexError:
            with open(FILE_PATH) as file:
                todo_list = file.readlines()

            print(f"The length of todo_list is {len(todo_list)}")
    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid action")