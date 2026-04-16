todo_list = []

while True:
    user_Action = input("Type add, show, edit, complete or exit: ")

    match user_Action:
        case "add":
            todo_item = input("Enter a todo item: ")
            todo_list.append(todo_item)
        case "show":
            for index, item in enumerate(todo_list):
                print(f"{index + 1}-{item}")
        case "edit":
            item_num = int(input("Enter the number of the item to edit: "))
            item_num -= 1
            todo_list[item_num] = input("Enter the new todo item: ")
        case "complete":
            item_num = int(input("Enter the number of the item to complete: "))
            item_num -= 1
            todo_list.pop(item_num)
        case "exit":
            break