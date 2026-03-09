user_prompt = "Type add or show: "

todo_list = []

while True:
    user_Action = input(user_prompt)

    match user_Action:
        case "add":
            todo_item = input("Enter a todo: ")
            todo_list.append(todo_item)

        case "show":
            print(todo_list)