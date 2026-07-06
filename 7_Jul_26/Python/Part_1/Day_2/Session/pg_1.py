todo_list = []

while True:
    user_action = input("Enter add, show or exit task: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            user_item = input("Enter todo: ")
            todo_list.append(user_item)
        case "show":
            for item in todo_list:
                print(item)
        case "exit":
            break


print("The program is closing.....")