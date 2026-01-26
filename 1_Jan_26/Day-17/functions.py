FILEPATH = './File/todo_list.txt'

def read_todo(filepath = FILEPATH):
    with open(filepath) as file:
        todo_local = file.readlines()
    return todo_local

def write_todo(todo_args, filepath = FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todo_args)