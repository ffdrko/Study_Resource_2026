# Experiment - 4 no print, no output
user_prompt = "Enter a todo: "
todo_list = []

while True:
    user_todo = input(user_prompt)
    print(user_todo.title())
    print(user_todo.capitalize())
    todo_list.append(user_todo)
    print(todo_list)