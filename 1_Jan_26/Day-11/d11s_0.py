FILE_PATH = '1_Jan_26/Day-11/File/todo_list.txt'

while True:
    user_action = input("Type add, show, edit, complete and exit: ")

    if user_action.startswith('add'):
        todo_item = user_action[4:] + "\n"

        with open(FILE_PATH) as file:
            todo_list = file.readlines()

        todo_list.append(todo_item)

        with open(FILE_PATH, 'w') as file:
            file.writelines(todo_list)

    elif user_action.startswith('show'):
        with open(FILE_PATH) as file:
            todo_list = file.readlines()
        
        for index, item in enumerate(todo_list):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")
    
    elif user_action.startswith('edit'):
        try:
            item_num = int(user_action[5:])
            with open(FILE_PATH) as file:
                todo_list = file.readlines()
            
            todo_list[item_num - 1] = input("Enter your new todo item: ") + "\n"

            with open(FILE_PATH, 'w') as file:
                file.writelines(todo_list)
        
        except ValueError:
            print("Afer edit you have enter number")
    
    elif user_action.startswith("complete"):
        try:
            item_num = int(user_action[9:])
            with open(FILE_PATH) as file:
                todo_list = file.readlines()
            
            todo_list.pop(item_num - 1)

            with open(FILE_PATH, 'w') as file:
                file.writelines(todo_list)
        
        except IndexError:
            print("The number is not inside the list.")
    elif user_action.startswith('exit'):
        break
    
    else:
        print('invalid comment')