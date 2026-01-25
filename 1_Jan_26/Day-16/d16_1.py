from d16s_0 import read_todo, write_todo
import time

time = time.strftime('%B %d, %Y %H:%M:%S')
print(f"It's {time}")

while True:
    user_action = input('Type add, show, edit, complete and exit: ')

    if user_action.startswith('add'):
        todo_item = user_action[4:] + '\n'
        todo_list = read_todo()
        todo_list.append(todo_item)

        write_todo(todo_list)
    
    elif user_action.startswith('show'):
        todo_list = read_todo()

        for index, item in enumerate(todo_list):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")
    
    elif user_action.startswith('edit'):
        item_num = int(user_action[5:]) - 1
        todo_list = read_todo()
        todo_list[item_num] = input("Enter new todo item: ") + '\n'
        write_todo(todo_list)
    
    elif user_action.startswith('complete'):
        item_num = int(user_action[9:]) -1
        todo_list = read_todo()
        todo_list.pop(item_num)
        write_todo(todo_list)
    
    elif user_action.startswith('exit'):
        break
    
    else:
        print("Command not valid.")