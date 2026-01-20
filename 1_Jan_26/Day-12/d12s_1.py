def get_todo(filepath):
    with open(filepath) as file:
        todo_local = file.readlines()
    return todo_local


while True:
    user_action = input("Type add, show, edit, complete or  exit: ").strip()

    if user_action.startswith('add'):
        todo_item = user_action[4:] + '\n'
        todo_list = get_todo('1_Jan_26/Day-12/File/todo_list.txt')

        todo_list.append(todo_item)

        with open('1_Jan_26/Day-12/File/todo_list.txt', 'w') as file:
            file.writelines(todo_list)
    
    elif user_action.startswith('show'):
        todo_list = get_todo('1_Jan_26/Day-12/File/todo_list.txt')

        for index, item in enumerate(todo_list):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")
    
    elif user_action.startswith('edit'):
        try:
            todo_num = int(user_action[5:]) - 1

            todo_list = get_todo('1_Jan_26/Day-12/File/todo_list.txt')
            todo_list[todo_num] = input("Enter new todo item: ") + '\n'

            with open('1_Jan_26/Day-12/File/todo_list.txt', 'w') as file:
                file.writelines(todo_list)
        
        except ValueError:
            print("Enter the item number after edit. Example-(edit 1)")
    
    elif user_action.startswith('complete'):
        try:
            todo_num = int(user_action[9:]) - 1

            todo_list = get_todo('1_Jan_26/Day-12/File/todo_list.txt')
            todo_list.pop(todo_num)

            with open('1_Jan_26/Day-12/File/todo_list.txt', 'w') as file:
                file.writelines(todo_list)
        
        except IndexError:
            print("The number is not in the list")
    
    elif user_action.startswith('exit'):
        break

    else:
        print("INVALID ACTION!!!")