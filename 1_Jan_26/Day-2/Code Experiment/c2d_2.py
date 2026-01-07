# capitalize vs title

todo = []

while True:
    user_prompt = "Enter a todo: "
    todo_item = input(user_prompt)
    todo.append(todo_item.title())
    print(todo)