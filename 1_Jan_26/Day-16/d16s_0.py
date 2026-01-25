FILEPATH = 'Day-16/File/todo_list.txt'

def read_todo(filepath = FILEPATH):
    with open(filepath) as file:
        local_list = file.readlines()
    return local_list


def write_todo(list_args, filepath = FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(list_args)


if __name__ == "__main__":
    print('This file contains all the functions.')