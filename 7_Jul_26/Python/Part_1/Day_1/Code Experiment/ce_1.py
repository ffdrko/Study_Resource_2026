
todo_list = []

while True:
    user_prompt = "Enter todo: "
    todo_item = input(user_prompt)
    print(todo_item.capitalize())
    todo_list.append(todo_item)
    print(todo_list)