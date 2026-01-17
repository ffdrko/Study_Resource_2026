FILE_PATH = "./Files/todo_list.txt"

while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    if 'add' in user_action:
        todo_item = user_action[4:] + '\n'

        with open(FILE_PATH) as file:
            todo_list = file.readlines()

        todo_list.append(todo_item)

        with open(FILE_PATH, 'w') as file:
            file.writelines(todo_list)

    elif 'show' in user_action:
        with open(FILE_PATH) as file:
            todo_list = file.readlines()

        for index, item in enumerate(todo_list):
            item = item.strip("\n")
            print(f"{index+1}-{item}")
    elif 'edit' in user_action:
        todo_item = int(user_action[5:])
        with open(FILE_PATH) as file:
            todo_list = file.readlines()

        todo_list[todo_item-1] = input("Enter new item to add: ") + '\n'

        with open(FILE_PATH, 'w') as file:
            file.writelines(todo_list)
    elif 'complete' in user_action:
        todo_num = int(user_action[9:]) - 1

        with open(FILE_PATH) as file:
            todo_list = file.readlines()

        todo_list.pop(todo_num)

        with open(FILE_PATH, "w") as file:
            file.writelines(todo_list)
    elif 'exit' in user_action:
        break
    else:
        print("Invalid action")