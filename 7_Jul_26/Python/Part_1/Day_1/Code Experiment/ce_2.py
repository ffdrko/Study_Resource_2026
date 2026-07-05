user_prompt = "Enter todo: "
todo_list = []

while True:
    todo_item = input(user_prompt)
    print(todo_item.capitalize())
    print(todo_item.title())
    todo_list.append(todo_item)
    print(todo_list)