from d14s_1 import get_todo, write_todo
while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    if user_action.startswith("add"):
        todo_item = user_action[4:] + "\n"
        todo_list = get_todo()
        todo_list.append(todo_item)
        write_todo(todo_list)
    
    elif user_action.startswith("show"):
        todo_list = get_todo()

        for index, item in enumerate(todo_list):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")

    elif user_action.startswith("edit"):
        item_num = int(user_action[5:])
        todo_list = get_todo()

        todo_list[item_num - 1] = input("Enter new todo item: ") + '\n'

        write_todo(todo_list)

    elif user_action.startswith('complete'):
        item_num = int(user_action[9:]) - 1
        todo_list = get_todo()

        todo_list.pop(item_num)

        write_todo(todo_list)

    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid comment!!")