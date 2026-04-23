# Experiment -1 use absolate file path
while True:
    user_action = input("Enter add, show, edit, complete or exit: ")

    match user_action:
        case "add":
            file = open("D:\FFD WORK\FFD\Study_Resource_2026/4_Apr_26\Part-2\Day_6\File/todo_list.txt", "r")
            todo_list =file.readlines()
            file.close()

            todo_item = input("Enter a todo item: ") + "\n"
            todo_list.append(todo_item)
            file = open("D:\FFD WORK\FFD\Study_Resource_2026/4_Apr_26\Part-2\Day_6\File/todo_list.txt", "w")
            file.writelines(todo_list)
            file.close()
        case 'show':
            file = open("D:\FFD WORK\FFD\Study_Resource_2026/4_Apr_26\Part-2\Day_6\File/todo_list.txt", "r")
            todo_list =file.readlines()
            file.close()
            for index, item in enumerate(todo_list):
                print(f"{index + 1}. {item}")
        case 'edit':
            item_num = int(input("Enter the number of the item to edit: "))
            item_num -= 1
            todo_list[item_num] = input("Enter the new todo item: ")
        case 'complete':
            item_num = int(input("Enter the number of the item to edit: "))
            item_num -= 1
            todo_list.pop(item_num)
        case 'exit':
            break