user_prompt = "Enter a todo: "
todo_list = []

while True:
    todo_item = input(user_prompt)
    print(todo_item.capitalize())
    todo_list.append(todo_item)