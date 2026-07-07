todo_list = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            user_item = input("Enter the todo: ")
            todo_list.append(user_item)
        case "show":
            for item in todo_list:
                print(item)
        case "edit":
            user_item_no = int(input("Enter the item you want to edit: "))
            user_item_no = user_item_no - 1
            todo_list[user_item_no] = input("Enter the new item to edit: ")
        case "exit":
            break
        case _:
            print("Invalid Input")

print("Bye!")