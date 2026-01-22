import functions as d14s_1
while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    if user_action.startswith("add"):
        todo_item = user_action[4:] + "\n"
        todo_list = d14s_1.get_todo()
        todo_list.append(todo_item)
        d14s_1.write_todo(todo_list)
    
    elif user_action.startswith("show"):
        todo_list = d14s_1.get_todo()

        for index, item in enumerate(todo_list):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")

    elif user_action.startswith("edit"):
        item_num = int(user_action[5:])
        todo_list = d14s_1.get_todo()

        todo_list[item_num - 1] = input("Enter new todo item: ") + '\n'

        d14s_1.write_todo(todo_list)

    elif user_action.startswith('complete'):
        item_num = int(user_action[9:]) - 1
        todo_list = d14s_1.get_todo()

        todo_list.pop(item_num)

        d14s_1.write_todo(todo_list)

    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid comment!!")