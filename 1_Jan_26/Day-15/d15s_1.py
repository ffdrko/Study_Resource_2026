from d15s_0 import get_todo_item, write_todo_item

while True:
    user_action = input("Type add, show, edit, complete and exit: ")

    if user_action.startswith('add'):
        todo_item = user_action[4:] + '\n'
        todo_list = get_todo_item()

        todo_list.append(todo_item)

        write_todo_item(todo_list)

    elif user_action.startswith('show'):
        todo_list = get_todo_item()

        for index, item in enumerate(todo_list):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")

    elif user_action.startswith('edit'):
        todo_item_num = int(user_action[5:]) - 1
        todo_list = get_todo_item()
        todo_list[todo_item_num] = input("Enter new edit item: ") + '\n'
        write_todo_item(todo_list)

    elif user_action.startswith('complete'):
        todo_item_num = int(user_action[9:]) - 1
        todo_list = get_todo_item()
        todo_list.pop(todo_item_num)
        write_todo_item(todo_list)

    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid input")