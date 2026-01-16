todo_list = []

while True:
    user_action = input("Type add, show, edit, complete or exit:")

    match user_action:
        case "add":
            todo_item = input("Enter a todo item: ") + "\n"

            file = open("1_Jan_26/Day-6/File/todo_list.txt", "r")
            todo_list = file.readlines()

            todo_list.append(todo_item)

            file = open("1_Jan_26/Day-6/File/todo_list.txt", "w")
            file.writelines(todo_list)
        
        case "show":
            file = open("1_Jan_26/Day-6/File/todo_list.txt", "r")
            todo_list = file.readlines()
            
            for index, item in enumerate(todo_list):
                print(f"{index + 1}-{item}")
        case "edit":
            item_number = int(input("Enter the number of the item to edit: "))
            item_number = item_number - 1
            todo_list[item_number] = input("Enter the new todo item: ")
        case "complete":
            item_number = int(input("Enter the number of the item is complete: "))
            item_number = item_number - 1
            todo_list.pop(item_number)
        case "exit":
            break