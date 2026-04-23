todo_list = []

while True:
    user_action = input("Enter add, show, edit or exit: ")
    
    match user_action:
        case "add":
            todo_item = input("Enter a todo item: ")
            todo_list.append(todo_item)
        case "show":
            for item in todo_list:
                print(item)
        case "edit":
            todo_item_num = int(input("Enter the number of the todo to edit: "))
            todo_item_num = todo_item_num - 1
            todo_list[todo_item_num] = input("Enter the new todo item: ") 
        case "exit":
            break