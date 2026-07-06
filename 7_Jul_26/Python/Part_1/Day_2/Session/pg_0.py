todo_list = []

while True:
    user_action = input("Enter add, show or exit task: ")

    match user_action:
        case "add":
            user_item = input("Enter todo: ")
            todo_list.append(user_item)
        case "show":
            print(todo_list)
        case "exit":
            break


print("The program is closing.....")