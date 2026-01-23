def get_todo_item(filepath = '.\file\todo_item.txt'):
    with open(filepath) as f:
        todo_local = f.readlines()
    return todo_local


def write_todo_item(todo_args, filepath = '.\file\todo_item.txt'):
    with open(filepath, 'w') as f:
        f.writelines(todo_args)


if __name__ == "__main__":
    print("This is the function files.")