# Experiment - 2 Inside vs Outside the Loop
user_prompt = "Enter a todo: "
todo_list = []

while True:
    user_todo = input(user_prompt)
    print(user_todo.capitalize())
    todo_list.append(user_todo)
    print(todo_list)